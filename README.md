# Covid-Tracker
COVID-19 that can send data to users via SMS

## How it works? 

This COVID-19 Tracker scrapes data from the Guardian.com's live COVID tracker. The scraper creates a dictionary with state being the key value and case count being the value. The web scraper is triggerd by Twillio API when a user sends an SMS to a certain number. The webscraper then retrieves the appropiate information depending on what state the user texted to the Twilio API and sends a response with the state count to the user with the Twillio API. 


