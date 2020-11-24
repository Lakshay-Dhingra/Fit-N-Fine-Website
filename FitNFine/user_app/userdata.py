from main_app.models import UserDetails

def getUserPublicDataDict(username):
    ud=UserDetails.objects.get(pk=username)
    di=dict()
    di["username"]=username
    di["firstname"]=ud.firstname
    di["lastname"]=ud.lastname
    di["email"]=ud.email

    user_type=ud.user_type
    about_me=ud.about_me
    if about_me == None or about_me == "":
        about_me="Hello! My Name is "+ud.firstname+". I am a "+user_type+"."
    di["about_me"]=about_me

    di["fitness_goal"]=ud.fitness_goal

    country=ud.country
    if country == "" or country == None:
        country="Unknown"
    di["country"]=country

    city=ud.city
    if city == "" or city == None:
        city="Unknown"
    di["city"]=city

    di["user_type"]=user_type

    age=ud.age
    if age==None:
        age="Unknown"
    di["age"]=age

    blood_group=ud.blood_group
    if blood_group=="U":
        blood_group="Unknown"
    di["blood_group"]=blood_group

    gender=ud.gender
    if gender=="U":
        gender="Unknown"
    elif gender=="M":
        gender="Male"
    elif gender=="F":
        gender=="Femlale"
    else:
        gender=="LGBTQ"
    di["gender"]=gender

    if ud.profile_pic == None or ud.profile_pic == "":
        di["profile_pic"]="https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png"
    else:
        di["profile_pic"]=ud.profile_pic.url
    
    di["created_at"]=ud.created_at
    di["total_points"]=ud.total_points
    di["level"],di["level_progress"]=getUserLevel(ud.total_points)
    di["above_level"]=di["level"]+1

    height=ud.height
    if height==None:
        weight=0
        height=1
    weight=ud.weight
    if weight==None:
        weight=0

    di["bmi"]="{:.2f}".format(weight/((height*0.0254)*(height*0.0254)))
    # password, phone, race, height, weight are not displayed in public
    return di

def getUserLevel(points):
    start=0
    slab=100
    level=0
    while(points>=start+slab):
        start+=slab
        slab+=20
        level+=1
    level_progress=round(((points-start)*100)/slab)
    if level_progress<0:
        level_progress=0
    return (level,level_progress)

