package main

import (
	"log"
	"net/http"
	"os"

	"github.com/joho/godotenv"
)

func main() {
	godotenv.Load()


	fs := http.FileServer(http.Dir("./assets"))
	port := "8080"
	if os.Getenv("PORT") != "" {
		port = os.Getenv("PORT")
	}
	log.Print("Listening on "+port)

	err := http.ListenAndServe(":"+port, fs)
	if err != nil {
		log.Fatal(err)
	}
}