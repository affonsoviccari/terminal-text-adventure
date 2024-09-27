from scenes import bedroom
import player

def describe(scene_name, noun):
    if scene_name.scene["nouns"][noun]["is_open"]:
        return scene_name.scene["nouns"][noun]["contents"]
    else: 
        return scene_name.scene["nouns"][noun]["description"]

def get_item(scene_name, item):
    """takes in scene name and command[1] from run_command func."""
    current_item = scene_name.scene["nouns"][item] 
    if item in scene_name.scene["nouns"] and current_item["can_get"]:
        player.stats["inventory"].append(item)
        scene_name.scene["nouns"].pop(item)
        print(f"You pick up the {item}") 
        return f"Your Inventory: {player.stats["inventory"]}"
    else: print("You cannot get that right now")
    
        

def open_item(scene_name, item):
    current_item = scene_name.scene["nouns"][item]
    if current_item["can_open"] and not current_item["is_open"]:
        current_item["is_open"] = True
        return f"You open the {item}."        
    elif current_item["can_open"] and current_item["is_open"]:
        return "It's already open!" 
    else: return f"You cannot open {item}"

def exit_scene(scene_name, noun):
    # todo: find way to pass next scene_name
    return f"you exit the {noun}"

verbs = {
    "look": {
        "func": describe
    },
    "get": {
        "func": get_item
    },
    "open": {
        "func": open_item
    },
    "exit": {
        "func": exit_scene
    }
}

