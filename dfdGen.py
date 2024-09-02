import os
from graphviz import Digraph

# Create 'images' folder if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Create directed graph
dfd = Digraph('KEMSA_Supply_Chain_DFD', node_attr={
              'style': 'rounded', 'fontsize': '12', 'fontname': 'Helvetica'})

# External Entities (rounded rectangles with different colors)
dfd.node('Hospitals/Clinics', 'Hospitals/Clinics', shape='rectangle',
         color='green', style='filled', fillcolor='lightgreen')
dfd.node('Suppliers', 'Suppliers', shape='rectangle',
         color='blue', style='filled', fillcolor='lightblue')

# KEMSA Process (central process with ellipse shape)
dfd.node('KEMSA', 'KEMSA Supply Chain Management',
         shape='ellipse', style='filled', color='lightblue')

# Data Stores (cylinder-shaped)
dfd.node('InventoryDB', 'Inventory Database', shape='cylinder',
         color='orange', style='filled', fillcolor='lightyellow')
dfd.node('DeliverySchedule', 'Delivery Schedule', shape='cylinder',
         color='orange', style='filled', fillcolor='lightyellow')
dfd.node('HistoricalData', 'Historical Data Store', shape='cylinder',
         color='orange', style='filled', fillcolor='lightyellow')

# Data Flows (connect edges with labels)
dfd.edge('Hospitals/Clinics', 'KEMSA', 'Supply Requests', color='black')
dfd.edge('KEMSA', 'Suppliers', 'Supply Order', color='black')
dfd.edge('Suppliers', 'KEMSA', 'Delivery Updates', color='black')
dfd.edge('KEMSA', 'Hospitals/Clinics', 'Supply Distribution', color='black')

dfd.edge('KEMSA', 'InventoryDB', 'Stock Data', color='gray')
dfd.edge('InventoryDB', 'KEMSA', 'Inventory Levels', color='gray')
dfd.edge('KEMSA', 'DeliverySchedule', 'Delivery Schedules', color='gray')
dfd.edge('DeliverySchedule', 'KEMSA', 'Delivery Plans', color='gray')
dfd.edge('KEMSA', 'HistoricalData', 'Supply & Delivery Records', color='gray')
dfd.edge('HistoricalData', 'KEMSA', 'Historical Data', color='gray')

# Save and render the diagram to the 'images' folder
dfd.render('images/KEMSA_Supply_Chain_DFD', format='png', cleanup=False)
