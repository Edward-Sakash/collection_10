"""ask - Combine lists into a dict
You are given two lists. One with color names (['red', 'green', 'blue']) and the other one with their RGB hex value (['#FF0000','#00FF00', '#0000FF']). Create a combined dict colors from those two lists so that for example printing colors['green'] shows #008000 on the screen.

Input:
color_names = ['red', 'green', 'blue']
color_hex = ['#FF0000','#00FF00', '#0000FF']
Output:
{
  'blue': '#0000FF', 
  'green': '#00FF00', 
  'red': '#FF0000'
}"""

# Solution 1

color_names = ['red', 'green', 'blue']
color_hex = ['#FF0000','#00FF00', '#0000FF']

# Combine the two lists into a dictionary using a dictionary comprehension
colors = {color_names[i]: color_hex[i] for i in range(len(color_names))}

# Print the resulting dictionary
print(colors)

print("____________________________________________")

# Solution 2

color_names = ['red', 'green', 'blue']
color_hex = ['#FF0000','#00FF00', '#0000FF']

# Combine the two lists into a dictionary using the zip function
colors = dict(zip(color_names, color_hex))

# Print the resulting dictionary
print(colors)
