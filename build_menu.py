#!/usr/bin/env python3

import rock_item as ritem

MAINMENU = {
    'main menu': ['hotspot', 'patches']
}

HOTSPOT = {
    'hotspot': ['activate', 'deactivate']
}

PATCHES = {
    'patches': []
}

menu = [MAINMENU, HOTSPOT, PATCHES]

"""menu"""

# main page

main_page = ritem.Page('main menu')

# hotspot page

hotspot_page = ritem.Page('hotpost')

# main page items

hotspot = ritem.Item('hotspot')
patches = ritem.Item('patches')

main_page.append(hotspot)
main_page.append(patches)

# hotspot page items

activate = ritem.Item('activate')
deactivate = ritem.Item('deactivate')

hotspot_page.append(activate)
hotspot_page.append(deactivate)

print(main_page.get_item_names())
print(hotspot_page.get_item_names())
