(ns hello-cljs.core)

(defn hi
  "Greets someone"
  [who]
  (let [msg (str "Hello, " who "!")]
    (println msg)))

; (println "Hello, ClojureScript!")


(hi "Joel")
