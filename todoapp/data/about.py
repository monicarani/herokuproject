from datetime import datetime
time=datetime.now().hour

if(time>=6 and time<12):
    greet="Morning"
    recipe="morning"
elif(time>=12 and time<16):
    greet="Afternoon"
    recipe="afternoon"
elif(time>=16 and time<=18):
    greet="Evening"
    recipe="evening"
elif(time>18 and time<=22):
    greet="Evening"
    recipe="night" 

bot ={"wish":greet,
    "morning":[{"no":1,"name":"Aloo Paratha","cost":30,"quantity":0},{"no":2,"name":"Semiya Upma","cost":35,"quantity":0},{"no":3,"name":"Masala Dosa","cost":25,"quantity":0},{"no":4,"name":"Poori","cost":20,"quantity":0},{"no":5,"name":"Idli(Sambar)","cost":20,"quantity":0},{"no":6,"name":"Vada","cost":15,"quantity":0},{"no":7,"name":"Ragi Rava Upma","cost":30,"quantity":0},{"no":8,"name":"Rava Utappam","cost":35,"quantity":0},{"no":9,"name":"Bread Omelette","cost":30,"quantity":0},{"no":10,"name":"Green Salad","cost":30,"quantity":0},{"no":11,"name":"Tea","cost":8,"quantity":0},{"no":12,"name":"Coffee","cost":7,"quantity":0}],
    "afternoon":[{"no":1,"name":"Veg Thali","cost":50,"quantity":0},{"no":2,"name":"Veg Biryani","cost":45,"quantity":0},{"no":3,"name":"Lemon Rice","cost":30,"quantity":0},{"no":4,"name":"Tomato Rice","cost":30,"quantity":0},{"no":5,"name":"Mushroom Biryani","cost":40,"quantity":0},{"no":6,"name":"Naan-Butter Paneer Masala","cost":40,"quantity":0},{"no":7,"name":"Non-Veg Thali","cost":60,"quantity":0},{"no":8,"name":"One-pot Chicken Biryani","cost":65,"quantity":0},{"no":9,"name":"Prawn Biryani","cost":70,"quantity":0},{"no":10,"name":"Curd Rice","cost":30,"quantity":0},{"no":11,"name":"Thumpsup","cost":15,"quantity":0},{"no":12,"name":"Sprite","cost":15,"quantity":0}],
    "evening":[{"no":1,"name":"Pav Bhaji","cost":30,"quantity":0},{"no":2,"name":"Paneer Tikka","cost":30,"quantity":0},{"no":3,"name":"Spring Rolls","cost":20,"quantity":0},{"no":4,"name":"Gobi Manchurian","cost":30,"quantity":0},{"no":5,"name":"Veg grilled Sandwich","cost":25,"quantity":0},{"no":6,"name":"Chilli Babycorn","cost":25,"quantity":0},{"no":7,"name":"Paneer naan Pizza","cost":35,"quantity":0},{"no":8,"name":"Egg Pakora","cost":35,"quantity":0},{"no":9,"name":"Fire Chicken","cost":40,"quantity":0},{"no":10,"name":"Fish 65","cost":50,"quantity":0},{"no":11,"name":"Tea","cost":8,"quantity":0},{"no":12,"name":"Coffee","cost":7,"quantity":0}],
    "night":[{"no":1,"name":"Tomato Soup","cost":30,"quantity":0},{"no":2,"name":"Veg corn Soup","cost":30,"quantity":0},{"no":3,"name":"Soya Salad","cost":35,"quantity":0},{"no":4,"name":"Pulka-mixed vegetable curry","cost":40,"quantity":0},{"no":5,"name":"Veg Thali","cost":50,"quantity":0},{"no":6,"name":"Vegetable Pulao","cost":45,"quantity":0},{"no":7,"name":"Chicken Fried Rice","cost":55,"quantity":0},{"no":8,"name":"Non-veg Thali","cost":60,"quantity":0},{"no":9,"name":"One-pot Mushroom Biryani","cost":50,"quantity":0},{"no":10,"name":"Curd Rice","cost":30,"quantity":0},{"no":11,"name":"Thumpsup","cost":15,"quantity":0},{"no":12,"name":"Sprite","cost":15,"quantity":0}],
    }

recipes={"menu":bot[recipe]}