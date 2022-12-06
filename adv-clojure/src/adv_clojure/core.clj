(ns adv-clojure.core
  [:require [clojure.java.io :as io]])


;; puzzle 1a
(def input1
  (->>  "input1.txt"
        (io/resource)
        slurp
        (clojure.string/split-lines)
        (partition-by #(= "" %))
        (map #(remove empty? %))))

(defn partition-reduce-add
  [input]
  (for [elf input]
    (->> elf
         (map #(Integer/parseInt %))
         (reduce +))))

(apply max (partition-reduce-add input1))

;; puzzle 1b
(defn remove-max
  [coll]
  (let [max-val (apply max coll)]
    (remove #(= max-val %) coll)))

(defn top-three
  [input]
  (let [elves (partition-reduce-add input1)
        max-elf (apply max elves)
        second-elf (apply max (remove-max elves))
        third-elf (apply max (remove-max (remove-max elves)))]
    (+ max-elf second-elf third-elf)))

(top-three input1)

;; TODO: tests, cli handling


;; puzzle 2a
(defn input-load
  [file-path]
  (->> file-path
       io/resource
       slurp))

(def input2
  (->> (input-load "input2.txt")
       clojure.string/split-lines
       (partition 1)))

;; a and x = rock 1 POINT
;; b and y = paper 2 POINTS
;; c and z = scissors 3 POINTS
;; win = 6 points
;; draw = 3 points
;; loss = 0 points

(defn score-hand
  [input]
  (let [opp (str (first input))
        you (str (last input))]
    (case opp
      "A" (case you
            "X" 4
            "Y" 8
            "Z" 3)
      "B" (case you
            "X" 1
            "Y" 5
            "Z" 9)
      "C" (case you
            "X" 7
            "Y" 2
            "Z" 6)
      :else "todo: log error")))

(reduce +
        (map #(score-hand (first %)) input2))

;; puzzle 2b
;; x = lose, y = draw, z = win
(defn re-score-hand
  [input]
  (let [opp (str (first input))
        you (str (last input))]
    (case opp
      "A" (case you
            "X" 3
            "Y" 4
            "Z" 8)
      "B" (case you
            "X" 1
            "Y" 5
            "Z" 9)
      "C" (case you
            "X" 2
            "Y" 6
            "Z" 7)
      :else "todo: log error")))

(reduce +
        (map #(re-score-hand (first %)) input2))

;; puzzle 3a
(def priorities
  (apply hash-map (interleave (flatten (conj (map char (range (int \A) (inc (int \Z))))
                                             (map char (range (int \a) (inc (int \z))))))
                              (range 1 53))))

(defn split-and-match
  [input-string]
  (let [split-list (split-at (/ (count input-string) 2) input-string)
        first-half (first split-list)
        second-half (last split-list)]
    (first (flatten (for [item first-half]
                      (filter #(= item %) second-half))))))

(reduce + (map #(priorities (split-and-match %))
               (clojure.string/split-lines (input-load "input3.txt"))))

;; puzzle 3b
(def elf-groups
  (partition 3 (clojure.string/split-lines (input-load "input3.txt"))))

(defn match-two
  [elf-group]
  (let [first-elf (first elf-group)
        second-elf (second elf-group)
        third-elf (last elf-group)
        first-match (flatten (for [item first-elf]
                               (filter #(= item %) second-elf)))]
    (first (flatten (for [item first-match]
                      (filter #(= item %) third-elf))))))

(reduce + (map #(priorities (match-two % ))
               elf-groups))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println "Hello, World!"))
