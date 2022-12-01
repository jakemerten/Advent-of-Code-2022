(ns adv-clojure.core
  [:require [clojure.java.io :as io]])


;; DAY 1
;; puzzle 1
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

;; puzzle 2
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



(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println "Hello, World!"))
