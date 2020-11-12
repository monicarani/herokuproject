
#This is the intents and handle page that returns the correct file by analyzing the input given.
def get_intent(message):
    m=message.lower()
    if "-" in m:
        return "done"
    elif "done" in m:
        return "paybill"
    elif "paid" in m:
        return "feedback"
    elif (len(m)==1 and (m>'0' and m<'6')):
        return "rating" 
    else:
        return "echo"


def handle(data):
    from flask import render_template
    from .data.about import bot,recipes
    intent = get_intent(data['message'])
    if intent == "done":
        sum=0
        l=data['message'].split(",")
        for i in l:
            num,quan=map(int,i.split("-"))
            recipes["menu"][num-1]["quantity"]=quan
            sum=sum+(recipes["menu"][num-1]["cost"]*quan)
        return render_template("messages/menugiven.html",question={"key":"confirmation"},recipes=recipes,sum=sum)
    elif intent == "paybill":
        for item in recipes["menu"]:
            item["quantity"]=0
        return render_template("messages/billpay.html",question={"key":"type paid"})
    elif intent == "feedback":
        return render_template("messages/feedback.html",question={"key":"rating"})
    elif intent == "rating":
        return render_template("messages/rating.html",data=int(data['message']))
    else:
        return render_template("messages/echo.html",data = data,bot=bot,recipes=recipes,question={"key":"order"})
