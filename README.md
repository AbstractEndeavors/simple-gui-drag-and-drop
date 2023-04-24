# simple-gui-drag-and-drop
This is a Python application that uses PySimpleGUI to create a graphical user interface for designing layouts using drag and drop features.

## Installation

1. Clone the repository or download the source files.
2. Install the required packages by running the following command:

## Usage

To run the application, simply execute the `main.py` file:


A window will appear, allowing you to drag and drop components onto a canvas to design your layout. You can also edit component attributes, such as size and color.

Once you have designed your layout, click the "Generate Layout" button to create a new window with the generated layout.

## License

This project is licensed under the MIT License.

PySimpleGUI==4.55.1

You can create a new file named "main.py" and copy the provided code into it. This will be the main file for your project.

Now you can create a new directory named "data" and a subdirectory named "parse_html" inside the "data" directory. Then, create a file named "js_total.json" inside the "parse_html" directory and add the JSON data required for the application.

Your project structure should look like this:

simple-gui-drag-and-drop/
    ├── main.py
    ├── README.md
    ├── requirements.txt
    └── data/
        └── parse_html/
            └── js_total.json

extended description:
Sure, here's a comprehensive description of the script and all non-standard functions:

The script is designed to create a GUI layout using the PySimpleGUI library by providing a drag-and-drop interface for designing the layout. It reads the available components and their attributes from a JSON file, and allows the user to modify these attributes as needed. Once the layout is designed, it generates the layout in a new window.

**Functions:**

1. `reader(place)`: This function reads the content of a file specified by the `place` parameter and returns its content.

2. `is_tuple_attribute(attr_value)`: This function checks if the given `attr_value` is a tuple or a string representing a tuple. Returns `True` if it is, otherwise `False`.

3. `convert_layout_to_components(generated_layout)`: This function takes a `generated_layout` and converts it into a list of PySimpleGUI components. It iterates through the layout, checking for each component type and creating the appropriate component with the given attributes.

4. `new_win(layout)`: This function creates a new window with the given `layout`. It displays the generated layout and waits for user interaction, such as closing the window or clicking the "Generate Layout" button.

5. `get_num_list()`: This function returns a list of numbers from 1 to 9 as strings.

6. `is_str(obj)`, `is_int(obj)`, `is_float(obj)`: These functions check if the given `obj` is a string, integer, or float, respectively, and return `True` or `False`.

7. `make_str(obj)`: This function converts the given `obj` into a string.

8. `is_number(obj)`: This function checks if the given `obj` is a number and returns `True` or `False`.

9. `get_type(obj)`: This function identifies the type of the given `obj`, converting it to the appropriate type (int, float, None, or str) and returning the converted value.

10. `layout_designer(components)`: This function creates the main layout designer window, which allows the user to drag and drop components onto a canvas, as well as modify the attributes of each component.

11. `create_all_ifs()`: This function generates the required `if` statements for all components in the input list.

12. `get_new_function(name)`: This function generates a new function definition for the given `name`.

The script starts by reading the components and their attributes from a JSON file (`js_total.json`) and creating a list of components. It then calls the `layout_designer` function with this list of components, allowing the user to design their layout using the drag-and-drop interface.

Once the user has completed designing their layout, the script generates the new layout and displays it in a new window by calling the `new_win` function.

Overall, the script provides a user-friendly interface for designing GUI layouts using the PySimpleGUI library and customizing the properties of each component.
