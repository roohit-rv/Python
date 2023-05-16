travel_log=[
   {
     "country": "France",
    "cities_visited":["Paris", "Lille", "Dijon"],
   "total_visits":12
   },
    {
      "country":"Germany",
      "cities_visited":["Berlin", "hamburg", "Stuttgart"],
     "total_visits":5
    }
    
  ]
def add_new_country(country, times, city):
     new_country={}
     new_country["country"]=country
     new_country["cities_visites"]=city
     new_country["total_visits"]=times
     travel_log.append(new_country)
            
add_new_country("Russia",2,["Moscow", "Saint-Petersburg"])
print(travel_log)