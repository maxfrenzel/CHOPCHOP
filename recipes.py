
# -*- coding: utf-8 -*-
'''
List of recipes as functions which initialise a list of steps
'''

# Correct integer division
from __future__ import division


import math

# Import class modules
import ingredients_JB as ing
import step as st
import vegetable as veg
import spice as spi
import other as oth
import liquid as liq
import fruit as fru
import dairy as dai
import meat as mea
import seafood as sea
import combined as com
import utensil as ute
import functions as fun

# Fake dynamic updating
import imp
imp.reload(ing)
imp.reload(st)
imp.reload(veg)
imp.reload(spi)
imp.reload(oth)
imp.reload(liq)
imp.reload(fru)
imp.reload(dai)
imp.reload(mea)
imp.reload(sea)
imp.reload(com)
imp.reload(ute)
imp.reload(fun)


# -------------------------------------------------
# -------------------------------------------------
# -------------------------------------------------
# Test dishes

# -------------------------------------------------
# -------------------------------------------------
# Salad

def Init_T01(guests, t_serve):

    # -------------------------------------------------
    # Ingredients
    
    #salt = spi.Salt(guests,0.2,"tsp")
    broccoli = veg.Broccoli(guests,100.0,"g")
    water_salad = liq.Water(guests,2000.0,"ml")
    ice_water = liq.Water(guests,1000.0,"ml",["ice"])
    almonds = oth.Almond(guests,25.0,"g",["chopped"])
    bacon = mea.Bacon(guests,25.0,"g",["cooked","crumbled"])
    red_onion = veg.OnionRed(guests,0.5)
    peas_salad = veg.Pea(guests,50.0,"g")
    mayonnaise = oth.Mayonnaise(guests,20.0,"g")
    vinegar = liq.Vinegar_Cider(guests, 0.4, "Tbsp")
    honey = oth.Honey(guests, 40.0, "g")
    
    # -------------------------------------------------
    # Utensils
    pan = ute.Pan()
    
    # -------------------------------------------------
    # Steps
    
    step1 = st.Step("Heat the pan for toasting the almonds.", [], [], [pan],[["heat"]])

    step2 = st.Step("Bring $qt1 water to a boil.", [water_salad], [["boil"]])
    
    step3 = st.Step("Cut the $qt1 broccoli into florets.", [broccoli], [["chop"]])
    
    step4 = st.Step("Toast the $qt1 almonds.", [almonds], [["toast"]], [], [], [step1])
    
    step5 = st.Step("Chop the $qt1 Red Onions.", [red_onion], [["chop"]])
    
    step6 = st.Step("Add the Broccoli florets to the boiling water.", [broccoli], [["boil"]], [], [], [step2,step3])
    
    step7 = st.Step("Pour a large bowl of ice water.", [ice_water], [["pour"]])
    
    step8 = st.Step("Drain the Broccoli and immediately put into the ice water to stop cooking. Leave for 30 seconds then drain and let dry.",\
                            [broccoli], [["drain"]], [], [], [step6,step7])
                            
    step9 = st.Step("Combine broccoli florets, almonds, crumbled bacon, chopped onion and peas in a large serving bowl.",\
                            [broccoli, almonds, bacon, red_onion, peas_salad], \
                            [["mix"],["mix"],["mix"],["mix"],["mix"]], [], [], [step4,step5,step8])
    salad_plain = step9.get_output("SuperIngredient")
    
    step10 = st.Step("In a bowl, whisk together $qt1 mayonnaise, $qt2 cider vinegar and $qt3 honey.",\
                            [mayonnaise, vinegar, honey], \
                            [["mix"],["mix"],["mix"]], [], [], [step4,step5,step8], {"flags":["whisk"], "output":["dressing"]})
    dressing = step10.get_output("Dressing")
    
    step11 = st.Step("Add dressing to the salad and toss to mix well. Season with salt and pepper and chill for at least 20 minutes before serving.",\
                            [salad_plain, dressing], \
                            [["mix"],["mix"]], [], [], [step9,step10], {"flags":["final"],"additional_bckg_time":20})
    salad = step11.get_output("Dish")
    
    step_serve = st.Step("Serve the salad.",\
                            [salad], [["serve"]], [], [], [step11], {"flags":["serve"], "serving_time":t_serve})
                            
    # -------------------------------------------------
    # Create list of steps
    
    dish_list = [step_serve]
    for i in range(11):
        string = "step" + str(i+1)
        exec("dish_list.append(" + string + ")")
        
    # -------------------------------------------------
    # Return list
    
    return dish_list
    
# -------------------------------------------------
# -------------------------------------------------
# Pasta

def Init_T02(guests, t_serve):
    # -------------------------------------------------
    # Ingredients
    
    pork_mince = mea.Mince(guests, 100.0, "g", ["pork"])
    onion = veg.Onion(guests, 0.25)
    water_pasta = liq.Water(guests,2000.0,"ml")
    garlic = veg.Garlic(guests, 1)
    lemon = fru.Lemon(guests, 0.125)
    parmesan = dai.Parmesan(guests, 12.5, "g")
    olive_oil = liq.Oil_Olive(guests, 0.25, "Tbsp")
    spaghetti = oth.Spaghetti(guests, 100.0, "g")
    double_cream = dai.Cream_Double(guests, 37.5, "ml")
    peas_pasta = veg.Pea(guests, 50.0, "g")
    parsley = spi.Parsley(guests, 20.0, "g")
    
    # -------------------------------------------------
    # Utensils
    pan = ute.Pan()
    
    # -------------------------------------------------
    # Steps
    
    step1 = st.Step("Grate $qt1 onions and put aside.", [onion], [["grate"]])

    step2 = st.Step("Crush $qt1 garlic cloves and put aside.", [garlic], [["crush"]])
    
    step3 = st.Step("Zest $qt1 lemon.", [lemon], [["zest"]])
    
    step4 = st.Step("Grate $qt1 parmesan.", [parmesan], [["grate"]])
    
    step5 = st.Step("Chop $qt1 parsley.", [parsley], [["chop"]])
    
    parmesan1 = parmesan * 0.5
    parmesan2 = parmesan * 0.5
    step6 = st.Step("Mix $qt1 mince with the onions, garlic, lemon zest and half of the parmesan.", [pork_mince,onion,garlic,lemon,parmesan1], \
                        [["mix"],["mix"],["mix"],["mix"],["mix"]], [], [], [step1,step2,step3,step4], \
                        {"flags":[], "output":["meatball_mix"],"step_max_time":20.0})
    meatball_mix = step6.get_output("SuperIngredient")
    
    step7 = st.Step("Shape into $num1 meatballs.", [meatball_mix], \
                        [["shape"]], [], [], [step6], \
                        {"flags":[], "output":["meatball"],"num_per_guest":4})
    meatballs = step7.get_output("Meatball")
    
    step8 = st.Step("Heat the pan for the meatballs.", [], [], [pan],[["heat"]])
    
    step9 = st.Step("Add $qt1 olive oil to the pan.", [olive_oil], [["add"]],\
                        [], [], [step8])
    
    step10 = st.Step("Put the $qt1 meatballs in the pan and start frying them.", [meatballs], [["fry"]],\
                        [], [], [step7,step9])                    
                                                                
    step11 = st.Step("Bring $qt1 water to a boil.", [water_pasta], [["boil"]])
    
    step12 = st.Step("The meatballs should be golden by now. Remove them from the pan and put aside.", [meatballs], [["remove"]],\
                        [], [], [step10])
                        
    step13 = st.Step("Add $qt1 spaghetti to the boiling water.", [spaghetti], [["boil"]],\
                        [], [], [step11]) 
                        
    step14 = st.Step("The pasta should be al dente now, drain it and put aside. Reserve " + str(guests*40) + "ml of the cooking water",\
                        [spaghetti], [["drain"]], [], [], [step13]) 
    pasta_cooking_water1 = liq.Water(guests,25.0,"ml",["pasta"])
    pasta_cooking_water2 = liq.Water(guests,15.0,"ml",["pasta"])
    
    step15 = st.Step("Add $qt1 cream and " + str(guests*25) + "ml of the pasta water to the meatballs, scraping the bottom of the pan to get all the sticky bits off. Let cook until meatballs are cooked through",\
                        [double_cream, pasta_cooking_water1, meatballs], [["mix"],["mix"],["mix"]], [], [], \
                        [step12,step14],{"flags":[], "output":["sauce"],"step_max_time":5.0})
    sauce = step15.get_output("SuperIngredient") 
    
    step16 = st.Step("Add $qt1 peas and the chopped parsley to the sauce",\
                        [sauce, peas_pasta, parsley], [["mix"],["mix"],["mix"]], [], [], \
                        [step5,step15],{"flags":[], "output":["sauce"],"step_max_time":2.0})
    sauce = step16.get_output("SuperIngredient") 
    
    step17 = st.Step("Add the pasta and the remainig " + str(guests*15) + " ml of pasta water to the sauce",\
                        [sauce, spaghetti, pasta_cooking_water2], [["mix"],["mix"],["mix"]], [], [], \
                        [step14,step16],{"flags":[], "output":["pasta"],"step_max_time":2.0})
    pasta = step17.get_output("SuperIngredient") 
    
    step18 = st.Step("Finally, stir the remaining half of the parmesan through the pasta.",\
                        [pasta, parmesan2], [["mix"],["mix"]], [], [], \
                        [step4,step17],{"flags":[], "output":["pasta"],"step_max_time":3.0})
    pasta = step18.get_output("Dish") 
    
    step_serve = st.Step("Serve the pasta.",\
                            [pasta], [["serve"]], [], [], [step18], {"flags":["serve"], "serving_time":t_serve})
                            
    # -------------------------------------------------
    # Create list of steps
    
    dish_list = [step_serve]
    for i in range(18):
        string = "step" + str(i+1)
        exec("dish_list.append(" + string + ")")
        
    # -------------------------------------------------
    # Return list
    
    return dish_list
 
    
       
             
# -------------------------------------------------
# -------------------------------------------------
# -------------------------------------------------
# All Time Favorites

    
# -------------------------------------------------
# -------------------------------------------------
# A1: Salade Niçoise with Samphire

def Init_A01(guests, t_serve):

    # -------------------------------------------------
    # Ingredients
    
    raw_tuna = ing.Ingredient(guests, 150.0, "g")
    sesame_seeds = ing.Ingredient(guests, 12.5, "g")
    sugarsnap_peas = ing.Ingredient(guests, 50.0, "g")
    samphire = ing.Ingredient(guests, 50.0, "g")
    rocket = ing.Ingredient(guests, 12.5, "g")
    cherry_tomato = ing.Ingredient(guests, 37.5, "g")
    ev_olive_oil = ing.Ingredient(guests, 0.25, "Tbsp")
    dijon_mustard = ing.Ingredient(guests, 0.25, "tsp")
    red_wine_vinegar = ing.Ingredient(guests, 0.75, "tbsp")
    flat_leaf_parsley = ing.Ingredient(guests, 1, "sprig")
    tarragon = ing.Ingredient(guests, 1, "sprig")
    olive_oil = liq.Oil_Olive(guests, 0.25, "Tbsp")
    garlic = veg.Garlic(guests, 0.25)
    lemon = fru.Lemon(guests, 0.13)
    
    # Extra-virgin olive oil vs. olive oil - let's distinguish between the two. Change olive oil to EVOO in A02 and A05
    # New units: specify "cloves" for garlic, add "sprig" for herbs
    
    # -------------------------------------------------
    # Utensils
    pan_fry = ute.Pan()
    large_pot = ute.Pot()
    # Add large pot for step X
    
    # -------------------------------------------------
    # Steps
    
    step1 = st.Step("Wash the sugar snaps, samphire, parsley, and tarragon. Peel the garlic cloves.", \
                    [sugarsnap_peas, samphire, flat_leaf_parsley, tarragon, garlic], [["wash"],["wash"],["wash"],["wash"],["peel"]], [], [], [], \
                    {"set_t_active":5.0, "set_t_bckg":0, "set_t_idle":20.0})
    
    step2 = st.Step("For the vinaigrette, combine $qt1 of garlic, $qt2 of dijon mustard, $qt3 of red wine vinegar, juice of $qt4 lemon, $qt5 of flat-leaf parsley, $qt6 of freh tarragon. Blend until smooth and add $qt7 extra virgin olive oil and pulse just until incorporated. Season with salt and pepper and set aside so the flavours can marry.",\
                    [garlic, dijon_mustard, red_wine_vinegar, lemon, flat_leaf_parsley, tarragon, ev_olive_oil], [["blend"],["blend"], ["blend"], ["squeeze"],["blend"],["blend"],["blend"]], [], [], [step1],\
                    {"set_t_active":5.0, "set_t_bckg":0, "set_t_idle":1440.0})
    vinaigrette = step2.get_output("SuperIngredient")
    
    step3 = st.Step("Salt a large pot of water and bring to a boil.",\
                    [], [], [large_pot], [["heat"]], [],\
                    {"set_t_active":0.5, "set_t_bckg":3.0, "set_t_idle":0.2})
    
    step4 = st.Step("Place $qt1 of sugar snaps and $qt2 of samphire into the boiling water. Cook for 2 min.",\
                    [sugarsnap_peas, samphire], [["boil"],["boil"]], [], [], [step1, step3],\
                    {"set_t_active":0.5, "set_t_bckg":2, "set_t_idle":0.5})
    
    step5 = st.Step("Remove the sugar snaps and samphire from the pot and rinse them with cold water until they've cooled down completely. Drain well.",\
                    [sugarsnap_peas, samphire], [["drain"],["drain"]], [], [], [step4],\
                    {"set_t_active":2.0, "set_t_bckg":3.0, "set_t_idle":20.0})
    greens_boiled = step5.get_output("SuperIngredient")
                    
    step6 = st.Step("Place $qt1 of sesame seeds on a plate and season generously with freshly ground black pepper. Cut the tuna in 200g pieces and press a piece of tuna into seed mixture to coat. Turn over and coat the other side. Repeat with remaining tuna.",\
                    [sesame_seeds, raw_tuna], [["arrange"],["season"]], [], [], [],\
                    {"set_t_active":1.0+0.8*guests, "set_t_bckg":0, "set_t_idle":5.0})
    tuna_seasoned = step6.get_output("SuperIngredient")
                                    
    step7 = st.Step("Preheat a large frying pan over a high heat.",\
                    [], [], [pan_fry], [["heat"]], [],\
                    {"set_t_active":0.1, "set_t_bckg":2, "set_t_idle":0.5})
                    
    step8 = st.Step("Add olive oil to the heated pan. Sear the tuna for 1 minute on each side for medium–rare.",\
                    [olive_oil, tuna_seasoned], [["add"],["fry"]], [],[], [step6,step7],\
                    {"set_t_active":3 * math.ceil(guests/3), "set_t_bckg":0, "set_t_idle":0.2})
    tuna_seared = step8.get_output("SuperIngredient")
                    
    step9 = st.Step("Take tuna off heat and let it cool for 5 minutes before slicing.",\
                    [tuna_seared], [["rest"]], [],[], [step8],\
                    {"set_t_active":0.5, "set_t_bckg":5.0, "set_t_idle":2.0})
                                    
    step10 = st.Step("Slice the cherry tomatoes in half. Arrange them with rocket leaves, sugar snaps and samphire on each plate.",\
                    [cherry_tomato, rocket, greens_boiled], [["cut"],["arrange"],["arrange"]], [],[], [step5],\
                    {"set_t_active":2.0+0.5*guests, "set_t_bckg":0, "set_t_idle":5.0})
    salad = step10.get_output("SuperIngredient")
                    
    step11 = st.Step("Slice the tuna in 0.5 cm thickness and arrange on top of the salad. Drizzle the vinaigrette.",\
                    [tuna_seared, salad, vinaigrette], [["cut"],["arrange"],["add"]], [],[], [step2, step9, step10],\
                    {"set_t_active":2.0+0.5*guests, "set_t_bckg":0, "set_t_idle":5.0})
    dish = step11.get_output("Dish")
    
    #step_serve = st.Step("Serve the salade ni" + u"\u00E7" + "oise.",\
    #                    [dish], [["serve"]], [], [], [step11], {"flags":["serve"], "serving_time":t_serve})
    step_serve = st.Step("Serve the salade nicoise.",\
                        [dish], [["serve"]], [], [], [step11], {"flags":["serve"], "serving_time":t_serve})
                            
    # -------------------------------------------------
    # Create list of steps
    
    dish_list = [step_serve]
    for i in range(11):
        string = "step" + str(i+1)
        exec("dish_list.append(" + string + ")")
        
    # -------------------------------------------------
    # Return list
    
    return dish_list

# -------------------------------------------------
# -------------------------------------------------
# A2: Pan-seared scallops with Saffron & Honey vinaigrette

def Init_A02(guests, t_serve):

    # -------------------------------------------------
    # Ingredients
    
    scallop = sea.Scallop(guests, 3.0)
    butter = dai.Butter(guests, 12.5, "g")
    lemon = fru.Lemon(guests, 0.25)
    olive_oil = liq.Oil_Olive(guests, 0.25, "Tbsp")
    apple = fru.Apple(guests, 0.25)
    watercress = veg.Watercress(guests, 12.5, "g")
    honey = oth.Honey(guests, 0.5,"Tbsp")
    saffron = spi.Saffron(guests, 0.25, "tsp")
    rice_wine_vinegar = liq.Vinegar_RiceWine(guests, 0.25, "Tbsp")
    aperol = liq.Aperol(guests, 0.25, "Tbsp")
    
    # -------------------------------------------------
    # Utensils
    #pan_sauce = ute.Pan()
    pan_fry = ute.Pan()
    #bowl = ute.Bowl()
    
    # -------------------------------------------------
    # Steps
    
    lemon_dressing = lemon * 0.5
    lemon_squeeze = lemon * 0.25
    
    step1 = st.Step("For the vinaigrette, mix $qt1 of honey, $qt2 of saffron threads and $qt3 rice wine vinegar in a small saucepan. Add $qt4 of Aperol and juice of $qt5 lemon.", \
                    [honey, saffron, rice_wine_vinegar, aperol, lemon_dressing], [["mix"],["mix"],["mix"],["mix"],["mix"]],\
                    [], [], [], {"set_t_active":4.0, "set_t_idle":1})
    dressing = step1.get_output("Dressing")
    
    step2 = st.Step("Warm the mixture over a low-medium heat, not letting it bubble or boil. Stir the liquid and watch the mixture take a golden shadow as the saffron infuses the mixture, about 5 min.",\
                    [dressing], [["heat","stir"]], [], [], [step1], {"set_t_active":5.0, "set_t_idle":0.1})
    
    step3 = st.Step("Give the vinaigrette a final stir and take the mixture off heat. Season with a pinch of salt and set aside.",\
                    [dressing], [["rest"]], [], [], [step2], {"set_t_active":0.5, "set_t_bckg":30, "set_t_idle":720})
    
    step4 = st.Step("Prep the salad by washing $qt1 of watercress and $qt2 apple. Peel the apple and cut it into thin matchsticks. Squeeze a few squirts of lemon juice and toss over the apple sticks and watercress.",\
                    [watercress, apple, lemon_squeeze], [["wash","mix"],["wash","cut","mix"],["squeeze"]], [], [], [],\
                    {"set_t_active":1*guests, "set_t_bckg":0, "set_t_idle":60})
    salad_prep = step4.get_output("SuperIngredient")
    
    step5 = st.Step("Preheat a large frying pan over medium-high heat.", [], [], [pan_fry],[["heat"]], [],\
                    {"set_t_active":0.1, "set_t_bckg":2, "set_t_idle":1})
    
    step6 = st.Step("Lightly season the scallops with salt and pepper.", [scallop], [["season"]], [], [], [],\
                    {"set_t_active":2, "set_t_bckg":0, "set_t_idle":5})
    
    step7 = st.Step("Add $qt1 butter to the heated pan. Add the scallops to the pan, frying them for 1.5 min on each side.",\
                    [butter, scallop], [["add"],["fry"]], [], [], [step5, step6],\
                    {"set_t_active":3 * math.ceil(guests/3), "set_t_bckg":0, "set_t_idle":0.1})
    scallops_cooked = step7.get_output("SuperIngredient")
    
    step8 = st.Step("Squeeze $qt1 lemon on the scallops and take off the heat.",\
                    [lemon_squeeze, scallops_cooked], [["squeeze"],["remove"]], [], [], [step6,step7],\
                    {"set_t_active":0.2, "set_t_bckg":0, "set_t_idle":2})
    scallops_done = step8.get_output("SuperIngredient")
                                                    
    step9 = st.Step("On each plate, arrange a bed of apple sticks and watercress in the middle and place 3 scallops per person. Mix in $qt1 of olive oil to the saffron honey vinaigrette and drizzle over each plate.",\
                    [salad_prep, scallops_done, olive_oil, dressing],\
                    [["arrange"],["arrange"],["mix"],["mix"]], [], [], [step3,step4,step8],\
                    {"set_t_active":3, "set_t_bckg":0, "set_t_idle":2})
    scallop_salad = step9.get_output("Dish")
    
    """step10 = st.Step("Mix in $qt1 of olive oil to the saffron honey vinaigrette. Drizzle over each plate.",\
                            [olive_oil, salad_plain, dressing], \
                            [["mix"],["mix"],["mix"]], [], [], [step3,step9],\
                            {"flags":["final"],"set_t_active":1, "set_t_bckg":0, "set_t_idle":0.1})
    salad = step10.get_output("Dish")"""
    
    step_serve = st.Step("Serve the scallops immediately.",\
                            [scallop_salad], [["serve"]], [], [], [step9], {"flags":["serve"], "serving_time":t_serve})
                            
    # -------------------------------------------------
    # Create list of steps
    
    dish_list = [step_serve]
    for i in range(9):
        string = "step" + str(i+1)
        exec("dish_list.append(" + string + ")")
        
    # -------------------------------------------------
    # Return list
    
    return dish_list
    
# -------------------------------------------------
# -------------------------------------------------
# A5: Crispy Pork Belly with roasted grapes

def Init_A05(guests, t_serve):

    # -------------------------------------------------
    # Ingredients
    
    pork_belly = mea.PorkBelly(guests, 300, "g")
    thyme = spi.Thyme(guests, 0.1, "bunch")
    rosemary = spi.Rosemary(guests,0.1, "bunch")
    bay_leaves = spi.BayLeave(guests,1.0)
    garlic = veg.Garlic(guests,1.0)
    olive_oil = liq.Oil_Olive(guests,25.0,"ml")
    vinegar = liq.Vinegar_Cider(guests, 0.5, "Tbsp")
    white_wine = liq.Wine_White(guests, 125.0,"ml")
    grapes = fru.Grapes(guests, 0.2, "bunch") 
    
    # -------------------------------------------------
    # Utensils
    oven = ute.Oven()
    
    # -------------------------------------------------
    # Steps
    
    step1 = st.Step("For the perfect crackling, boil some water and pour it over the pork skin. Drain the water.", \
                    [pork_belly], [["none"]], [], [], [], \
                    {"set_t_active":4.0, "set_t_bckg":0, "set_t_idle":1})
    
    step2 = st.Step("Brush the belly with $qt1 of cider vinegar and rub it into the skin. Leave it uncovered in the fridge for 2 hours, preferably overnight.",\
                    [vinegar, pork_belly], [["brush", "chill"],["brush"]], [], [], [step1],\
                    {"set_t_active":3.0, "set_t_bckg":120.0, "set_t_idle":1200.0})
    belly_brushed = step2.get_output("SuperIngredient")
    
    step3 = st.Step("Pre-heat the oven to 200°C/Gas Mark 6.",\
                    [], [], [oven], [["heat"]], [],\
                    {"set_t_active":0.5, "set_t_bckg":20, "set_t_idle":30})
    
    step4 = st.Step("Wash and roughly chop $qt1 of thyme and $qt2 of rosemary. Peel $qt3 garlic cloves.",\
                    [thyme,rosemary,garlic], [["wash", "chop"],["wash", "chop"],["peel"]], [], [], [],\
                    {"set_t_active":0.8*guests, "set_t_bckg":0, "set_t_idle":10})
    
    step5 = st.Step("Put the herbs, garlic, and olive oil in the blender. Blend well.",\
                    [thyme,rosemary,garlic,olive_oil], [["blend"],["blend"],["blend"],["blend"]], [],[], [step4],\
                    {"set_t_active":2, "set_t_bckg":0, "set_t_idle":20})
    herb_mix = step5.get_output("SuperIngredient")
    
    step6 = st.Step("In an oven tray, place the pork belly skin-side down and season lightly with salt and pepper. Rub the herb mixture all over the top. Turn the meat skin-side up. Use a paper towl to pat the skin dry. Season the skin lightly with sea salt.",\
                    [belly_brushed,herb_mix], [["season"],["season"]], [],[], [step2, step5],\
                    {"set_t_active":2*(guests**0.5), "set_t_bckg":0, "set_t_idle":5})
    belly_seasoned = step6.get_output("SuperIngredient")
                                    
    """step7 = st.Step("Turn the meat skin-side up. Use a paper towl to pat the skin dry. Season the skin lightly with sea salt.",\
                    [belly_seasoned], [["season"]], [],[], [step6],\
                    {"set_t_active":2*(guests**0.1), "set_t_bckg":0, "set_t_idle":5})"""
                    
    step7 = st.Step("Place the tray in the oven and roast for 50 min.",\
                    [belly_seasoned], [["roast"]], [],[], [step3,step6],\
                    {"set_t_active":1, "set_t_bckg":50, "set_t_idle":1})
                    
    step8 = st.Step("The skin will have formed some crackling by now. Gently pour $qt1 of white wine into the tray (not touching the skin) along with the $qt2 bay leaves. Cover the belly with foil to prevent the skin from turning black.",\
                    [white_wine, bay_leaves, belly_seasoned], [["add"],["add"],["roast"]], [],[], [step7],\
                    {"set_t_active":2, "set_t_bckg":0, "set_t_idle":1})
    pork_jus = step8.get_output("SuperIngredient")
                                    
    step9 = st.Step("Turn the oven down to 180°C/Gas Mark 4 and continue roasting the meat for another hour.",\
                    [pork_jus], [["roast"]], [],[], [step8],\
                    {"set_t_active":0.5, "set_t_bckg":60, "set_t_idle":1})
                    
    step10 = st.Step("Turn the oven down to 110°C/Gas Mark 1/4. Throw in small clusters of grapes to roast together in jus and continue roasting for another 20 min until the skin has formed a complete crackling.",\
                    [pork_jus, grapes], [["roast"],["roast"]], [],[], [step9],\
                    {"set_t_active":2, "set_t_bckg":20, "set_t_idle":1})
    pork_done = step10.get_output("SuperIngredient")
    
    step11 = st.Step("Remove the pork from the oven and let it rest for 10 minutes.",\
                    [pork_done], [["remove"]], [],[], [step10],\
                    {"set_t_active":0.5, "set_t_bckg":10, "set_t_idle":2})
    
    step12 = st.Step("Cut the belly into decent sized squares per person and arrange with the jus, bay leaves and roasted grapes.",\
                            [pork_done],\
                            [["arrange"]], [], [], [step11],\
                            {"flags":["final"],"set_t_active":1*(guests**0.8), "set_t_bckg":0, "set_t_idle":0.1})
    dish = step12.get_output("Dish")
    
    step_serve = st.Step("Serve the pork.",\
                            [dish], [["serve"]], [], [], [step12], {"flags":["serve"], "serving_time":t_serve})
                            
    # -------------------------------------------------
    # Create list of steps
    
    dish_list = [step_serve]
    for i in range(12):
        string = "step" + str(i+1)
        exec("dish_list.append(" + string + ")")
        
    # -------------------------------------------------
    # Return list
    
    return dish_list
    
# -------------------------------------------------
# -------------------------------------------------
# A8: Mint Chocolate tart with pistachios

def Init_A08(guests, t_serve):

    # -------------------------------------------------
    # Ingredients
    
    icing_sugar = oth.IcingSugar(guests,10,"g")
    cocoa_powder = oth.CocoaPowder(guests, 7.50,"g")
    flour = oth.Flour(guests,20,"g")
    butter = dai.Butter(guests,13.00,"g",["chilled"])
    egg_yolk = oth.Egg_Yolk(guests,0.25)
    chocolate = oth.Chocolate_Dark(guests,25,"g")
    double_cream = dai.Cream_Double(guests,25,"ml")
    mint = spi.Mint(guests,0.2,"bunch")
    pistachio = oth.Pistachio(guests,5.0)
    
    # -------------------------------------------------
    # Utensils
    oven = ute.Oven()
    baking_paper = ute.Utensil()
    
    # -------------------------------------------------
    # Steps
    
    step1 = st.Step("For the tart case, put $qt1 of icing sugar, $qt2 of cocoa powder, $qt3 of flour, and $qt4 of small cubes of chilled butter into a large bowl. Rub the butter into the dry ingredients with fingertips. The mixture will look like breadcrumbs.", \
                    [icing_sugar, cocoa_powder, flour, butter], [["mix"],["mix"],["mix"],["mix"]], [], [], [], \
                    {"set_t_active":5.0, "set_t_bckg":0, "set_t_idle":20.0})
    dough1 = step1.get_output("SuperIngredient")
    
    step2 = st.Step("Add $qt1 egg yolk into the mixture and form a ball. Wrap the dough in clingfilm and chill in the fridge for 30 min.",\
                    [egg_yolk, dough1], [["mix"],["mix", "chill"]], [], [], [step1],\
                    {"set_t_active":3.0, "set_t_bckg":30.0, "set_t_idle":30.0})
    dough2 = step2.get_output("SuperIngredient")
    
    step3 = st.Step("To make the ganache, put $qt1 broken chocolate pieces in a heatproof bowl. Heat $qt2 double cream and $qt3 mint in a small saucepan, until bubbles form at the edges.",\
                    [chocolate, double_cream, mint], [["cut"],["heat"],["heat"]], [], [], [],\
                    {"set_t_active":5, "set_t_bckg":0, "set_t_idle":0.2})
    
    step4 = st.Step("Strain the heated cream and pour onto the chocolate. Stir until chocolate melts and combines with the cream.",\
                    [chocolate, double_cream, mint], [["mix"],["mix"],["mix"]], [], [], [step3],\
                    {"set_t_active":4.0, "set_t_bckg":0, "set_t_idle":5.0})
    ganache = step4.get_output("SuperIngredient")
    
    step5 = st.Step("Let the ganache cool, then chill in the fridge for 1 hour.",\
                    [ganache], [["rest","chill"]], [],[], [step4],\
                    {"set_t_active":1.0, "set_t_bckg":90.0, "set_t_idle":10.0})
                    
    step6 = st.Step("Pre-heat the oven to 170°C/Gas Mark 3.",\
                    [], [], [oven], [["heat"]], [],\
                    {"set_t_active":0.5, "set_t_bckg":10.0, "set_t_idle":30.0})
                                    
    step7 = st.Step("Take out the chilled dough. Cut the dough into " + str(guests) + " equal pieces and flatten them. Place the dough in each tartlet case and press the dough against the tartlet tin to shape. The dough should be roughly 3 mm in thickness.",\
                    [dough2], [["arrange"]], [],[], [step2],\
                    {"set_t_active":3.0+1.5*(guests), "set_t_bckg":0, "set_t_idle":15.0})
                    
    step8 = st.Step("Cut out discs of baking paper and place on the dough. Put a baking bean on top in each tartlet case. Put the tartlets in the oven and bake for 10 min.",\
                    [dough2], [["bake"]], [],[], [step6,step7],\
                    {"set_t_active":1.0+0.5*guests, "set_t_bckg":10.0, "set_t_idle":0.2})
                    
    step9 = st.Step("Remove the paper and beans from the tartlets and bake for 2 more min.",\
                    [dough2], [["bake"]], [],[], [step8],\
                    {"set_t_active":1, "set_t_bckg":2.0, "set_t_idle":0.1})
                                    
    step10 = st.Step("Take tart cases out of the oven and leave to cool for at least 30 min at room temperature.",\
                    [dough2], [["rest"]], [],[], [step9],\
                    {"set_t_active":0.5, "set_t_bckg":30.0, "set_t_idle":2000.0})
                    
    step11 = st.Step("Unmould the pastry cases and fill them with chocolate ganache.",\
                    [dough2, ganache], [["mix"],["mix"]], [],[], [step5, step10],\
                    {"set_t_active":1.0+1.0*guests, "set_t_bckg":0, "set_t_idle":10.0})
    tart = step11.get_output("SuperIngredient")
    
    step12 = st.Step("Coarsely chop the pistachios and garnish the tart with them. If the tart is soft, refrigerate for 30 min to ensure the tart is firm.",\
                    [pistachio,tart], [["chop"],["garnish"]], [],[], [step11],\
                    {"set_t_active":3+0.25*guests, "set_t_bckg":30.0, "set_t_idle":300.0})
    tart_garnished = step12.get_output("Dish")
    
    """step13 = st.Step("Before serving the tarts, take out of the fridge for at least 20 min.",\
                    [tart_garnished], [["arrange"]], [], [], [step12],\
                    {"flags":["final"],"set_t_active":0.5, "set_t_bckg":20.0, "set_t_idle":180.0})
    dish = step13.get_output("Dish")"""
    
    step_serve = st.Step("Serve the tarts.",\
                        [tart_garnished], [["serve"]], [], [], [step12], {"flags":["serve"], "serving_time":t_serve})
                            
    # -------------------------------------------------
    # Create list of steps
    
    dish_list = [step_serve]
    for i in range(12):
        string = "step" + str(i+1)
        exec("dish_list.append(" + string + ")")
        
    # -------------------------------------------------
    # Return list
    
    return dish_list