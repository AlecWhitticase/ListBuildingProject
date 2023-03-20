import random

UNIT_LIST = []

def add_unit(name,points,slot):
    "Creates a unit and adds that unit to the pool. Touple."
    if type(name) == str and type(points) == int:
        unit_list = [name,points,slot]
        UNIT_LIST.append(unit_list)
        return unit_list
    else:
        print("Information provided was incorrect.")



def list_gen(UNIT_LIST):
    "generates the list"
    total_cost = 0
    army = []
    hq,troop,elite,fast,heavy = catagory(UNIT_LIST)
    print(hq)
    if len(hq) == 0:
            print("You need at least one hq")
            return(None)
    else:
        army.append(hq[random.randint(0,len(hq))])
        total_cost += hq[0][1]
    print("1 = Troops, 2 = Elites, 3 = Fast, 4 = heavy")
    ark_slot = input("What's your ark slot comrade")
    while total_cost < 2000:
        if ark_slot == 1:
            if len[army] > 4:
                new_troop = troop[random.randint(0,len(troop))]
                army.append(new_troop)
                total_cost += new_troop[1]
        if ark_slot == 2:
            if len[army] > 4:
                new_elite = elite[random.randint(0,len(elite))]
                army.append(new_elite)
                total_cost += new_elite[1]
        if ark_slot == 3:
            if len[army] > 4:
                new_fast = fast[random.randint(0,len(fast))]
                army.append(new_fast)
                total_cost += new_fast[1]
        if ark_slot == 4:
            if len[army] > 4:
                new_heavy = heavy[random.randint(0,len(heavy))]
                army.append(new_heavy)
                total_cost += new_heavy[1]
        else:
            new_unit_type = random.randit(0,4)
            if new_unit_type == 0:
                if len(hq) != 0:
                    new_hq = hq[random.randint(0,len(hq))]
                    army.append(new_hq)
                    total_cost += new_hq[1]
            if new_unit_type == 1:
                if len(troop) != 0:
                    new_troop = troop[random.randint(0,len(troop))]
                    army.append(new_troop)
                    total_cost += new_troop[1]
            if new_unit_type == 2:
                if len(elite) != 0:
                    new_elite = elite[random.randint(0,len(elite))]
                    army.append(new_elite)
                    total_cost += new_elite[1]
            if new_unit_type == 3:
                if len(fast) != 0:
                    new_fast = fast[random.randint(0,len(fast))]
                    army.append(new_fast)
                    total_cost += new_fast[1]
            if new_unit_type == 4:
                if len(heavy) != 0:
                    new_heavy = heavy[random.randint(0,len(heavy))]
                    army.append(new_heavy)
                    total_cost += new_heavy[1]
    return army
                       

        

def catagory(units):
    "subdivides the units avaible."
    hq = []
    troop = []
    elite = []
    fast = []
    heavy = []
    for unit in units:
        slot = unit[2]
        if slot == 1:
            hq.append(unit)
        elif slot == 2:
            troop.append(unit)
        elif slot == 3:
            elite.append(unit)
        elif slot == 4:
            fast.append(unit)
        elif slot == 5:
            heavy.append(unit)
    return(hq,troop,elite,fast,heavy)


    


def main():
    while True:
        next_action = int(input("1 to add a unit, 2 to generate, 3 to print current pool"))
        if next_action == 1:
            unit_name = str(input("Unit Name ")) 
            unit_cost = int(input("Unit Cost "))
            print("1 = HQ, 2 = Troops, 3 = Elites, 4 = Fast, 5 = heavy")
            unit_slot = str(input("slot "))
            add_unit(unit_name,unit_cost,unit_slot)
        elif next_action == 2:
            rand_list = list_gen(UNIT_LIST)
            print(rand_list)
        elif next_action == 3:
            print(UNIT_LIST)


master_of_possession = ["MoP",500,1]
Noise_Marine = ["noise marine",500,2]
UNIT_LIST=[master_of_possession,Noise_Marine,Noise_Marine,Noise_Marine]
main()