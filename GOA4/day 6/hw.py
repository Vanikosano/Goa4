#--------------------------------------------------------------------#

#მომხმარებლის ნიშნებისგან გამოანგარიშება საშუალო არითმეტიკული და თუ ცხრაზე მეტი იქნება:
#დაუპრინტეთ გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები
#თუ ეს იქნება 5ზე ნაკლები: დაუპრინტე გილოცავ გაექეცი მატრიცას
#თუ იქნება 5 იდან 9 მდე: დაუპრინტე YOU ARE MID
#თუ იქნება 10ზე მეტი ან 0ზე ნაკლები: დაუპრინტე there is something wrong with you

#--------------------------------------------------------------------#

user_rating = int(input("შეიყვანე შენი ნიშანი: "))
average_rating = user_rating / 2

if average_rating > 9:
    print("გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები.")
else:
    if 0 < average_rating < 5:
        print("გილოცავ შენ გაიქეცი მატრიციდან.")
    else:
        if 5 <= average_rating <= 9:
            print("YOU ARE MID")
        else:
            print("There is something wrong with you")

#--------------------------------------------------------------------#

# მომხმარებელს შეეკითხეთ ხელფასი
# თუ 10000ზე მეტია, დაუპრინტეთ, გოა-ში სწავლობდი?
# თუ 1000----10000 -ია , დაუპრინტეთ you mid
# თუ 1000-ზე დაბალია, დაუპრინტეთ, შემოსულიყავი გოაში, მატრიცელო

#--------------------------------------------------------------------#

salary = int(input("რა არის შენი ხელფასი? "))

if salary > 10000:
    print("გოაში სწავლობდი?")
else:
    if 1000 <= salary <= 10000:
        print("you are mid")
    else:
        print("შემოსულიყავი გოაში მატრიცელო")

#--------------------------------------------------------------------#