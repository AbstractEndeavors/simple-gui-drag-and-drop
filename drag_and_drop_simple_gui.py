import PySimpleGUI as sg
import json

def reader(place):
    f = open(place)
    return f.read()
def is_tuple_attribute(attr_value):
    if isinstance(attr_value, tuple):
        return True
    elif isinstance(attr_value, str) and attr_value.startswith("(") and attr_value.endswith(")"):
        return True
    return False

def convert_layout_to_components(generated_layout):
    components = []

    for item in generated_layout:
        component_type = item['component']
        text_id = item.get('text_id', None)
        size = item['size']
    js = generated_layout[0]
    keys = list(js.keys())
    for k in range(0,len(keys)):
        js[keys[k]] =get_type(js[keys[k]])
   
    if component_type == 'Text':
        components.append(sg.Text(text_id, size=size))
    elif component_type == 'Input':
        components.append(sg.Input(size=size, key=f'-{text_id}-'))
    elif component_type == 'Button':
        button_text = item.get('button_text', text_id)  # Get the button_text attribute
        components.append(sg.Button(button_text, size=size))
    elif component_type == 'Multiline':
        components.append(sg.Multiline(size=size, key=f'-{text_id}-'))
    elif component_type == 'Listbox':
            components.append(sg.Listbox(values=js["values"],default_values=js["default_values"],select_mode=js["select_mode"],change_submits=js["change_submits"],enable_events=js["enable_events"],bind_return_key=js["bind_return_key"],size=js["size"],s=js["s"],disabled=js["disabled"],justification=js["justification"],auto_size_text=js["auto_size_text"],font=js["font"],no_scrollbar=js["no_scrollbar"],horizontal_scroll=js["horizontal_scroll"],background_color=js["background_color"],text_color=js["text_color"],highlight_background_color=js["highlight_background_color"],highlight_text_color=js["highlight_text_color"],sbar_trough_color=js["sbar_trough_color"],sbar_background_color=js["sbar_background_color"],sbar_arrow_color=js["sbar_arrow_color"],sbar_width=js["sbar_width"],sbar_arrow_width=js["sbar_arrow_width"],sbar_frame_color=js["sbar_frame_color"],sbar_relief=js["sbar_relief"],key=js["key"],k=js["k"],pad=js["pad"],p=js["p"],tooltip=js["tooltip"],expand_x=js["expand_x"],expand_y=js["expand_y"],right_click_menu=js["right_click_menu"],visible=js["visible"],metadata=js["metadata"]))
    elif component_type == 'CalendarButton':
            components.append(sg.CalendarButton(button_text=js["button_text"],target=js["target"],close_when_date_chosen=js["close_when_date_chosen"],default_date_m_d_y=js["default_date_m_d_y"],image_filename=js["image_filename"],image_data=js["image_data"],image_size=js["image_size"],image_subsample=js["image_subsample"],tooltip=js["tooltip"],border_width=js["border_width"],size=js["size"],s=js["s"],auto_size_button=js["auto_size_button"],button_color=js["button_color"],disabled=js["disabled"],font=js["font"],bind_return_key=js["bind_return_key"],focus=js["focus"],pad=js["pad"],p=js["p"],key=js["key"],k=js["k"],locale=js["locale"],format=js["format"],begin_at_sunday_plus=js["begin_at_sunday_plus"],month_names=js["month_names"],day_abbreviations=js["day_abbreviations"],title=js["title"],no_titlebar=js["no_titlebar"],location=js["location"],visible=js["visible"],metadata=js["metadata"],expand_x=js["expand_x"],expand_y=js["expand_y"],default_color=js["default_color"],file_types=js["file_types"],initial_folder=js["initial_folder"],change_submits=js["change_submits"],enable_events=js["enable_events"],default_extension=js["default_extension"],files_delimiter=js["files_delimiter"]))
    elif component_type == 'Pane':
            components.append(sg.Pane(pane_list=js["pane_list"],background_color=js["background_color"],size=js["size"],s=js["s"],pad=js["pad"],p=js["p"],orientation=js["orientation"],show_handle=js["show_handle"],relief=js["relief"],handle_size=js["handle_size"],border_width=js["border_width"],key=js["key"],k=js["k"],expand_x=js["expand_x"],expand_y=js["expand_y"],visible=js["visible"],metadata=js["metadata"]))
    elif component_type == 'show_debugger_popout_window':
            components.append(sg.show_debugger_popout_window(location=js["location"]))
    elif component_type == 'Text':
            components.append(sg.Text(text=js["text"],size=js["size"],s=js["s"],auto_size_text=js["auto_size_text"],click_submits=js["click_submits"],enable_events=js["enable_events"],relief=js["relief"],font=js["font"],text_color=js["text_color"],background_color=js["background_color"],border_width=js["border_width"],justification=js["justification"],pad=js["pad"],p=js["p"],key=js["key"],k=js["k"],right_click_menu=js["right_click_menu"],expand_x=js["expand_x"],expand_y=js["expand_y"],grab=js["grab"],tooltip=js["tooltip"],visible=js["visible"],metadata=js["metadata"]))
    elif component_type == 'Column':
            components.append(sg.Column(layout=js["layout"],background_color=js["background_color"],size=js["size"],s=js["s"],size_subsample_width=js["size_subsample_width"],size_subsample_height=js["size_subsample_height"],pad=js["pad"],p=js["p"],scrollable=js["scrollable"],vertical_scroll_only=js["vertical_scroll_only"],right_click_menu=js["right_click_menu"],key=js["key"],k=js["k"],visible=js["visible"],justification=js["justification"],element_justification=js["element_justification"],vertical_alignment=js["vertical_alignment"],grab=js["grab"],expand_x=js["expand_x"],expand_y=js["expand_y"],metadata=js["metadata"],sbar_trough_color=js["sbar_trough_color"],sbar_background_color=js["sbar_background_color"],sbar_arrow_color=js["sbar_arrow_color"],sbar_width=js["sbar_width"],sbar_arrow_width=js["sbar_arrow_width"],sbar_frame_color=js["sbar_frame_color"],sbar_relief=js["sbar_relief"]))
    elif component_type == 'UserSettings':
            components.append(sg.UserSettings(filename=js["filename"],path=js["path"],silent_on_error=js["silent_on_error"],autosave=js["autosave"],use_config_file=js["use_config_file"],convert_bools_and_none=js["convert_bools_and_none"]))
    elif component_type == 'VPush':
            components.append(sg.VPush(background_color=js["background_color"]))
    elif component_type == 'read_all_windows':
            components.append(sg.read_all_windows(timeout=js["timeout"],timeout_key=js["timeout_key"]))
    elif component_type == 'clipboard_set':
            components.append(sg.clipboard_set(new_value=js["new_value"]))
    elif component_type == 'main_get_debug_data':
            components.append(sg.main_get_debug_data(suppress_popup=js["suppress_popup"]))
    elif component_type == 'Combo':
            components.append(sg.Combo(values=js["values"],default_value=js["default_value"],size=js["size"],s=js["s"],auto_size_text=js["auto_size_text"],background_color=js["background_color"],text_color=js["text_color"],button_background_color=js["button_background_color"],button_arrow_color=js["button_arrow_color"],bind_return_key=js["bind_return_key"],change_submits=js["change_submits"],enable_events=js["enable_events"],disabled=js["disabled"],key=js["key"],k=js["k"],pad=js["pad"],p=js["p"],expand_x=js["expand_x"],expand_y=js["expand_y"],tooltip=js["tooltip"],readonly=js["readonly"],font=js["font"],visible=js["visible"],metadata=js["metadata"]))
    elif component_type == 'ChangeLookAndFeel':
            components.append(sg.ChangeLookAndFeel(index=js["index"],force=js["force"],columns=js["columns"],scrollable=js["scrollable"],scroll_area_size=js["scroll_area_size"],search_string=js["search_string"],location=js["location"]))
    elif component_type == 'pin':
            components.append(sg.pin(elem=js["elem"],vertical_alignment=js["vertical_alignment"],shrink=js["shrink"],expand_x=js["expand_x"],expand_y=js["expand_y"],elem_or_row=js["elem_or_row"],background_color=js["background_color"]))
    elif component_type == 'Canvas':
            components.append(sg.Canvas(canvas=js["canvas"],background_color=js["background_color"],size=js["size"],s=js["s"],pad=js["pad"],p=js["p"],key=js["key"],k=js["k"],tooltip=js["tooltip"],right_click_menu=js["right_click_menu"],expand_x=js["expand_x"],expand_y=js["expand_y"],visible=js["visible"],border_width=js["border_width"],metadata=js["metadata"]))
    elif component_type == 'ButtonMenu':
            components.append(sg.ButtonMenu(button_text=js["button_text"],menu_def=js["menu_def"],tooltip=js["tooltip"],disabled=js["disabled"],image_source=js["image_source"],image_filename=js["image_filename"],image_data=js["image_data"],image_size=js["image_size"],image_subsample=js["image_subsample"],image_zoom=js["image_zoom"],border_width=js["border_width"],size=js["size"],s=js["s"],auto_size_button=js["auto_size_button"],button_color=js["button_color"],background_color=js["background_color"],text_color=js["text_color"],disabled_text_color=js["disabled_text_color"],font=js["font"],item_font=js["item_font"],pad=js["pad"],p=js["p"],expand_x=js["expand_x"],expand_y=js["expand_y"],key=js["key"],k=js["k"],tearoff=js["tearoff"],visible=js["visible"],metadata=js["metadata"]))
    elif component_type == 'set_options':
            components.append(sg.set_options(icon=js["icon"],button_color=js["button_color"],element_size=js["element_size"],button_element_size=js["button_element_size"],margins=js["margins"],element_padding=js["element_padding"],auto_size_text=js["auto_size_text"],auto_size_buttons=js["auto_size_buttons"],font=js["font"],border_width=js["border_width"],slider_border_width=js["slider_border_width"],slider_relief=js["slider_relief"],slider_orientation=js["slider_orientation"],autoclose_time=js["autoclose_time"],message_box_line_width=js["message_box_line_width"],progress_meter_border_depth=js["progress_meter_border_depth"],progress_meter_style=js["progress_meter_style"],progress_meter_relief=js["progress_meter_relief"],progress_meter_color=js["progress_meter_color"],progress_meter_size=js["progress_meter_size"],text_justification=js["text_justification"],background_color=js["background_color"],element_background_color=js["element_background_color"],text_element_background_color=js["text_element_background_color"],input_elements_background_color=js["input_elements_background_color"],input_text_color=js["input_text_color"],scrollbar_color=js["scrollbar_color"],text_color=js["text_color"],element_text_color=js["element_text_color"],debug_win_size=js["debug_win_size"],window_location=js["window_location"],error_button_color=js["error_button_color"],tooltip_time=js["tooltip_time"],tooltip_font=js["tooltip_font"],use_ttk_buttons=js["use_ttk_buttons"],ttk_theme=js["ttk_theme"],suppress_error_popups=js["suppress_error_popups"],suppress_raise_key_errors=js["suppress_raise_key_errors"],suppress_key_guessing=js["suppress_key_guessing"],warn_button_key_duplicates=js["warn_button_key_duplicates"],enable_treeview_869_patch=js["enable_treeview_869_patch"],enable_mac_notitlebar_patch=js["enable_mac_notitlebar_patch"],use_custom_titlebar=js["use_custom_titlebar"],titlebar_background_color=js["titlebar_background_color"],titlebar_text_color=js["titlebar_text_color"],titlebar_font=js["titlebar_font"],titlebar_icon=js["titlebar_icon"],user_settings_path=js["user_settings_path"],pysimplegui_settings_path=js["pysimplegui_settings_path"],pysimplegui_settings_filename=js["pysimplegui_settings_filename"],keep_on_top=js["keep_on_top"],dpi_awareness=js["dpi_awareness"],scaling=js["scaling"],disable_modal_windows=js["disable_modal_windows"],force_modal_windows=js["force_modal_windows"],tooltip_offset=js["tooltip_offset"],sbar_trough_color=js["sbar_trough_color"],sbar_background_color=js["sbar_background_color"],sbar_arrow_color=js["sbar_arrow_color"],sbar_width=js["sbar_width"],sbar_arrow_width=js["sbar_arrow_width"],sbar_frame_color=js["sbar_frame_color"],sbar_relief=js["sbar_relief"],alpha_channel=js["alpha_channel"],hide_window_when_creating=js["hide_window_when_creating"],use_button_shortcuts=js["use_button_shortcuts"],watermark_text=js["watermark_text"]))
    elif component_type == 'Spin':
            components.append(sg.Spin(values=js["values"],initial_value=js["initial_value"],disabled=js["disabled"],change_submits=js["change_submits"],enable_events=js["enable_events"],readonly=js["readonly"],size=js["size"],s=js["s"],auto_size_text=js["auto_size_text"],bind_return_key=js["bind_return_key"],font=js["font"],background_color=js["background_color"],text_color=js["text_color"],key=js["key"],k=js["k"],pad=js["pad"],p=js["p"],wrap=js["wrap"],tooltip=js["tooltip"],right_click_menu=js["right_click_menu"],expand_x=js["expand_x"],expand_y=js["expand_y"],visible=js["visible"],metadata=js["metadata"]))
    elif component_type == 'Input':
            components.append(sg.Input(default_text=js["default_text"],size=js["size"],s=js["s"],disabled=js["disabled"],password_char=js["password_char"],justification=js["justification"],background_color=js["background_color"],text_color=js["text_color"],font=js["font"],tooltip=js["tooltip"],border_width=js["border_width"],change_submits=js["change_submits"],enable_events=js["enable_events"],do_not_clear=js["do_not_clear"],key=js["key"],k=js["k"],focus=js["focus"],pad=js["pad"],p=js["p"],use_readonly_for_disable=js["use_readonly_for_disable"],readonly=js["readonly"],disabled_readonly_background_color=js["disabled_readonly_background_color"],disabled_readonly_text_color=js["disabled_readonly_text_color"],selected_text_color=js["selected_text_color"],selected_background_color=js["selected_background_color"],expand_x=js["expand_x"],expand_y=js["expand_y"],right_click_menu=js["right_click_menu"],visible=js["visible"],metadata=js["metadata"]))
    elif component_type == 'StatusBar':
            components.append(sg.StatusBar(text=js["text"],size=js["size"],s=js["s"],auto_size_text=js["auto_size_text"],click_submits=js["click_submits"],enable_events=js["enable_events"],relief=js["relief"],font=js["font"],text_color=js["text_color"],background_color=js["background_color"],justification=js["justification"],pad=js["pad"],p=js["p"],key=js["key"],k=js["k"],right_click_menu=js["right_click_menu"],expand_x=js["expand_x"],expand_y=js["expand_y"],tooltip=js["tooltip"],visible=js["visible"],metadata=js["metadata"]))
    elif component_type == 'execute_editor':
            components.append(sg.execute_editor(command=js["command"],args=js["*args"],wait=js["wait"],cwd=js["cwd"],pipe_output=js["pipe_output"],merge_stderr_with_stdout=js["merge_stderr_with_stdout"],stdin=js["stdin"],file_to_edit=js["file_to_edit"],line_number=js["line_number"],folder_to_open=js["folder_to_open"],subprocess_id=js["subprocess_id"],timeout=js["timeout"],pyfile=js["pyfile"],parms=js["parms"],interpreter_command=js["interpreter_command"]))
    elif component_type == 'theme':
            components.append(sg.theme(new_theme=js["new_theme"],new_theme_name=js["new_theme_name"],new_theme_dict=js["new_theme_dict"],color=js["color"],columns=js["columns"],scrollable=js["scrollable"],scroll_area_size=js["scroll_area_size"],search_string=js["search_string"],location=js["location"]))
    elif component_type == 'Checkbox':
            components.append(sg.Checkbox(text=js["text"],default=js["default"],size=js["size"],s=js["s"],auto_size_text=js["auto_size_text"],font=js["font"],background_color=js["background_color"],text_color=js["text_color"],checkbox_color=js["checkbox_color"],highlight_thickness=js["highlight_thickness"],change_submits=js["change_submits"],enable_events=js["enable_events"],disabled=js["disabled"],key=js["key"],k=js["k"],pad=js["pad"],p=js["p"],tooltip=js["tooltip"],right_click_menu=js["right_click_menu"],expand_x=js["expand_x"],expand_y=js["expand_y"],visible=js["visible"],metadata=js["metadata"]))
    elif component_type == 'HorizontalSeparator':
            components.append(sg.HorizontalSeparator(color=js["color"],pad=js["pad"],p=js["p"],key=js["key"],k=js["k"]))
    elif component_type == 'one_line_progress_meter_cancel':
            components.append(sg.one_line_progress_meter_cancel(title=js["title"],current_value=js["current_value"],max_value=js["max_value"],args=js["*args"],key=js["key"],orientation=js["orientation"],bar_color=js["bar_color"],button_color=js["button_color"],size=js["size"],border_width=js["border_width"],grab_anywhere=js["grab_anywhere"],no_titlebar=js["no_titlebar"],keep_on_top=js["keep_on_top"],no_button=js["no_button"]))
    elif component_type == 'Sizegrip':
            components.append(sg.Sizegrip(background_color=js["background_color"],pad=js["pad"],p=js["p"],key=js["key"],k=js["k"]))
    elif component_type == 'Table':
            components.append(sg.Table(values=js["values"],headings=js["headings"],visible_column_map=js["visible_column_map"],col_widths=js["col_widths"],cols_justification=js["cols_justification"],def_col_width=js["def_col_width"],auto_size_columns=js["auto_size_columns"],max_col_width=js["max_col_width"],select_mode=js["select_mode"],display_row_numbers=js["display_row_numbers"],starting_row_number=js["starting_row_number"],num_rows=js["num_rows"],row_height=js["row_height"],font=js["font"],justification=js["justification"],text_color=js["text_color"],background_color=js["background_color"],alternating_row_color=js["alternating_row_color"],selected_row_colors=js["selected_row_colors"],header_text_color=js["header_text_color"],header_background_color=js["header_background_color"],header_font=js["header_font"],header_border_width=js["header_border_width"],header_relief=js["header_relief"],row_colors=js["row_colors"],vertical_scroll_only=js["vertical_scroll_only"],hide_vertical_scroll=js["hide_vertical_scroll"],border_width=js["border_width"],sbar_trough_color=js["sbar_trough_color"],sbar_background_color=js["sbar_background_color"],sbar_arrow_color=js["sbar_arrow_color"],sbar_width=js["sbar_width"],sbar_arrow_width=js["sbar_arrow_width"],sbar_frame_color=js["sbar_frame_color"],sbar_relief=js["sbar_relief"],size=js["size"],change_submits=js["change_submits"],enable_events=js["enable_events"],enable_click_events=js["enable_click_events"],right_click_selects=js["right_click_selects"],bind_return_key=js["bind_return_key"],pad=js["pad"],p=js["p"],key=js["key"],k=js["k"],tooltip=js["tooltip"],right_click_menu=js["right_click_menu"],expand_x=js["expand_x"],expand_y=js["expand_y"],visible=js["visible"],metadata=js["metadata"]))
    elif component_type == 'SystemTray':
            components.append(sg.SystemTray(menu=js["menu"],filename=js["filename"],data=js["data"],data_base64=js["data_base64"],tooltip=js["tooltip"],metadata=js["metadata"]))
    elif component_type == 'Popup':
            components.append(sg.Popup(args=js["*args"],title=js["title"],button_color=js["button_color"],background_color=js["background_color"],text_color=js["text_color"],button_type=js["button_type"],auto_close=js["auto_close"],auto_close_duration=js["auto_close_duration"],custom_text=js["custom_text"],non_blocking=js["non_blocking"],icon=js["icon"],line_width=js["line_width"],font=js["font"],no_titlebar=js["no_titlebar"],grab_anywhere=js["grab_anywhere"],location=js["location"],relative_location=js["relative_location"],keep_on_top=js["keep_on_top"],any_key_closes=js["any_key_closes"],image=js["image"],modal=js["modal"],right_justify_buttons=js["right_justify_buttons"],button_justification=js["button_justification"],drop_whitespace=js["drop_whitespace"],image_source=js["image_source"],message=js["message"],alpha_channel=js["alpha_channel"],time_between_frames=js["time_between_frames"],transparent_color=js["transparent_color"],default_path=js["default_path"],default_extension=js["default_extension"],save_as=js["save_as"],multiple_files=js["multiple_files"],file_types=js["file_types"],no_window=js["no_window"],size=js["size"],initial_folder=js["initial_folder"],files_delimiter=js["files_delimiter"],history=js["history"],show_hidden=js["show_hidden"],history_setting_filename=js["history_setting_filename"],default_text=js["default_text"],password_char=js["password_char"],yes_no=js["yes_no"],no_buttons=js["no_buttons"],no_sizegrip=js["no_sizegrip"]))
    elif component_type == 'OptionMenu':
            components.append(sg.OptionMenu(values=js["values"],default_value=js["default_value"],size=js["size"],s=js["s"],disabled=js["disabled"],auto_size_text=js["auto_size_text"],expand_x=js["expand_x"],expand_y=js["expand_y"],background_color=js["background_color"],text_color=js["text_color"],key=js["key"],k=js["k"],pad=js["pad"],p=js["p"],tooltip=js["tooltip"],visible=js["visible"],metadata=js["metadata"]))
    elif component_type == 'popup':
            components.append(sg.popup(args=js["*args"],title=js["title"],button_color=js["button_color"],background_color=js["background_color"],text_color=js["text_color"],button_type=js["button_type"],auto_close=js["auto_close"],auto_close_duration=js["auto_close_duration"],custom_text=js["custom_text"],non_blocking=js["non_blocking"],icon=js["icon"],line_width=js["line_width"],font=js["font"],no_titlebar=js["no_titlebar"],grab_anywhere=js["grab_anywhere"],location=js["location"],relative_location=js["relative_location"],keep_on_top=js["keep_on_top"],any_key_closes=js["any_key_closes"],image=js["image"],modal=js["modal"],right_justify_buttons=js["right_justify_buttons"],button_justification=js["button_justification"],drop_whitespace=js["drop_whitespace"],image_source=js["image_source"],message=js["message"],alpha_channel=js["alpha_channel"],time_between_frames=js["time_between_frames"],transparent_color=js["transparent_color"],messages=js["*messages"],emoji=js["emoji"],start_mon=js["start_mon"],start_day=js["start_day"],start_year=js["start_year"],begin_at_sunday_plus=js["begin_at_sunday_plus"],close_when_chosen=js["close_when_chosen"],locale=js["locale"],month_names=js["month_names"],day_abbreviations=js["day_abbreviations"],day_font=js["day_font"],mon_year_font=js["mon_year_font"],arrow_font=js["arrow_font"],default_path=js["default_path"],default_extension=js["default_extension"],save_as=js["save_as"],multiple_files=js["multiple_files"],file_types=js["file_types"],no_window=js["no_window"],size=js["size"],initial_folder=js["initial_folder"],files_delimiter=js["files_delimiter"],history=js["history"],show_hidden=js["show_hidden"],history_setting_filename=js["history_setting_filename"],default_text=js["default_text"],password_char=js["password_char"],window=js["window"],element=js["element"],menu_def=js["menu_def"],display_duration_in_ms=js["display_duration_in_ms"],fade_in_duration=js["fade_in_duration"],alpha=js["alpha"],yes_no=js["yes_no"],no_buttons=js["no_buttons"],no_sizegrip=js["no_sizegrip"]))
    elif component_type == 'MenubarCustom':
            components.append(sg.MenubarCustom(menu_definition=js["menu_definition"],disabled_text_color=js["disabled_text_color"],bar_font=js["bar_font"],font=js["font"],tearoff=js["tearoff"],pad=js["pad"],p=js["p"],background_color=js["background_color"],text_color=js["text_color"],bar_background_color=js["bar_background_color"],bar_text_color=js["bar_text_color"],key=js["key"],k=js["k"]))
    elif component_type == 'RButton':
            components.append(sg.RButton(button_text=js["button_text"],image_filename=js["image_filename"],image_data=js["image_data"],image_size=js["image_size"],image_subsample=js["image_subsample"],tooltip=js["tooltip"],size=js["size"],s=js["s"],auto_size_button=js["auto_size_button"],button_color=js["button_color"],font=js["font"],bind_return_key=js["bind_return_key"],disabled=js["disabled"],focus=js["focus"],pad=js["pad"],p=js["p"],key=js["key"],k=js["k"],border_width=js["border_width"],metadata=js["metadata"],expand_x=js["expand_x"],expand_y=js["expand_y"]))
    elif component_type == 'Tree':
            components.append(sg.Tree(data=js["data"],headings=js["headings"],visible_column_map=js["visible_column_map"],col_widths=js["col_widths"],col0_width=js["col0_width"],col0_heading=js["col0_heading"],def_col_width=js["def_col_width"],auto_size_columns=js["auto_size_columns"],max_col_width=js["max_col_width"],select_mode=js["select_mode"],show_expanded=js["show_expanded"],change_submits=js["change_submits"],enable_events=js["enable_events"],click_toggles_select=js["click_toggles_select"],font=js["font"],justification=js["justification"],text_color=js["text_color"],border_width=js["border_width"],background_color=js["background_color"],selected_row_colors=js["selected_row_colors"],header_text_color=js["header_text_color"],header_background_color=js["header_background_color"],header_font=js["header_font"],header_border_width=js["header_border_width"],header_relief=js["header_relief"],num_rows=js["num_rows"],row_height=js["row_height"],vertical_scroll_only=js["vertical_scroll_only"],hide_vertical_scroll=js["hide_vertical_scroll"],sbar_trough_color=js["sbar_trough_color"],sbar_background_color=js["sbar_background_color"],sbar_arrow_color=js["sbar_arrow_color"],sbar_width=js["sbar_width"],sbar_arrow_width=js["sbar_arrow_width"],sbar_frame_color=js["sbar_frame_color"],sbar_relief=js["sbar_relief"],pad=js["pad"],p=js["p"],key=js["key"],k=js["k"],tooltip=js["tooltip"],right_click_menu=js["right_click_menu"],expand_x=js["expand_x"],expand_y=js["expand_y"],visible=js["visible"],metadata=js["metadata"]))
    elif component_type == 'Frame':
            components.append(sg.Frame(title=js["title"],layout=js["layout"],title_color=js["title_color"],background_color=js["background_color"],title_location=js["title_location"],relief=js["relief"],size=js["size"],s=js["s"],font=js["font"],pad=js["pad"],p=js["p"],border_width=js["border_width"],key=js["key"],k=js["k"],tooltip=js["tooltip"],right_click_menu=js["right_click_menu"],expand_x=js["expand_x"],expand_y=js["expand_y"],grab=js["grab"],visible=js["visible"],element_justification=js["element_justification"],vertical_alignment=js["vertical_alignment"],metadata=js["metadata"]))
    elif component_type == 'get_versions':
            components.append(sg.get_versions())
    elif component_type == 'Multiline':
            components.append(sg.Multiline(default_text=js["default_text"],enter_submits=js["enter_submits"],disabled=js["disabled"],autoscroll=js["autoscroll"],autoscroll_only_at_bottom=js["autoscroll_only_at_bottom"],border_width=js["border_width"],size=js["size"],s=js["s"],auto_size_text=js["auto_size_text"],background_color=js["background_color"],text_color=js["text_color"],selected_text_color=js["selected_text_color"],selected_background_color=js["selected_background_color"],horizontal_scroll=js["horizontal_scroll"],change_submits=js["change_submits"],enable_events=js["enable_events"],do_not_clear=js["do_not_clear"],key=js["key"],k=js["k"],write_only=js["write_only"],auto_refresh=js["auto_refresh"],reroute_stdout=js["reroute_stdout"],reroute_stderr=js["reroute_stderr"],reroute_cprint=js["reroute_cprint"],echo_stdout_stderr=js["echo_stdout_stderr"],focus=js["focus"],font=js["font"],pad=js["pad"],p=js["p"],tooltip=js["tooltip"],justification=js["justification"],no_scrollbar=js["no_scrollbar"],wrap_lines=js["wrap_lines"],sbar_trough_color=js["sbar_trough_color"],sbar_background_color=js["sbar_background_color"],sbar_arrow_color=js["sbar_arrow_color"],sbar_width=js["sbar_width"],sbar_arrow_width=js["sbar_arrow_width"],sbar_frame_color=js["sbar_frame_color"],sbar_relief=js["sbar_relief"],expand_x=js["expand_x"],expand_y=js["expand_y"],rstrip=js["rstrip"],right_click_menu=js["right_click_menu"],visible=js["visible"],metadata=js["metadata"]))
    elif component_type == 'Image':
            components.append(sg.Image(source=js["source"],filename=js["filename"],data=js["data"],background_color=js["background_color"],size=js["size"],s=js["s"],pad=js["pad"],p=js["p"],key=js["key"],k=js["k"],tooltip=js["tooltip"],subsample=js["subsample"],zoom=js["zoom"],right_click_menu=js["right_click_menu"],expand_x=js["expand_x"],expand_y=js["expand_y"],visible=js["visible"],enable_events=js["enable_events"],metadata=js["metadata"]))
    elif component_type == 'running_windows':
            components.append(sg.running_windows())
    elif component_type == 'easy_print':
            components.append(sg.easy_print(args=js["*args"],size=js["size"],end=js["end"],sep=js["sep"],location=js["location"],relative_location=js["relative_location"],font=js["font"],no_titlebar=js["no_titlebar"],no_button=js["no_button"],grab_anywhere=js["grab_anywhere"],background_color=js["background_color"],text_color=js["text_color"],keep_on_top=js["keep_on_top"],do_not_reroute_stdout=js["do_not_reroute_stdout"],echo_stdout=js["echo_stdout"],colors=js["colors"],c=js["c"],resizable=js["resizable"],erase_all=js["erase_all"],blocking=js["blocking"],wait=js["wait"]))
    elif component_type == 'Window':
            components.append(sg.Window(title=js["title"],layout=js["layout"],default_element_size=js["default_element_size"],default_button_element_size=js["default_button_element_size"],auto_size_text=js["auto_size_text"],auto_size_buttons=js["auto_size_buttons"],relative_location=js["relative_location"],location=js["location"],size=js["size"],element_padding=js["element_padding"],margins=js["margins"],button_color=js["button_color"],font=js["font"],progress_bar_color=js["progress_bar_color"],background_color=js["background_color"],border_depth=js["border_depth"],auto_close=js["auto_close"],auto_close_duration=js["auto_close_duration"],icon=js["icon"],force_toplevel=js["force_toplevel"],alpha_channel=js["alpha_channel"],return_keyboard_events=js["return_keyboard_events"],use_default_focus=js["use_default_focus"],text_justification=js["text_justification"],no_titlebar=js["no_titlebar"],grab_anywhere=js["grab_anywhere"],grab_anywhere_using_control=js["grab_anywhere_using_control"],keep_on_top=js["keep_on_top"],resizable=js["resizable"],disable_close=js["disable_close"],disable_minimize=js["disable_minimize"],right_click_menu=js["right_click_menu"],transparent_color=js["transparent_color"],debugger_enabled=js["debugger_enabled"],right_click_menu_background_color=js["right_click_menu_background_color"],right_click_menu_text_color=js["right_click_menu_text_color"],right_click_menu_disabled_text_color=js["right_click_menu_disabled_text_color"],right_click_menu_selected_colors=js["right_click_menu_selected_colors"],right_click_menu_font=js["right_click_menu_font"],right_click_menu_tearoff=js["right_click_menu_tearoff"],finalize=js["finalize"],element_justification=js["element_justification"],ttk_theme=js["ttk_theme"],use_ttk_buttons=js["use_ttk_buttons"],modal=js["modal"],enable_close_attempted_event=js["enable_close_attempted_event"],enable_window_config_events=js["enable_window_config_events"],titlebar_background_color=js["titlebar_background_color"],titlebar_text_color=js["titlebar_text_color"],titlebar_font=js["titlebar_font"],titlebar_icon=js["titlebar_icon"],use_custom_titlebar=js["use_custom_titlebar"],scaling=js["scaling"],sbar_trough_color=js["sbar_trough_color"],sbar_background_color=js["sbar_background_color"],sbar_arrow_color=js["sbar_arrow_color"],sbar_width=js["sbar_width"],sbar_arrow_width=js["sbar_arrow_width"],sbar_frame_color=js["sbar_frame_color"],sbar_relief=js["sbar_relief"],watermark=js["watermark"],metadata=js["metadata"]))
    elif component_type == 'user_settings_delete_entry':
            components.append(sg.user_settings_delete_entry(key=js["key"],silent_on_error=js["silent_on_error"],filename=js["filename"],path=js["path"],default=js["default"],value=js["value"],settings_dict=js["settings_dict"]))
    elif component_type == 'Sizer':
            components.append(sg.Sizer(h_pixels=js["h_pixels"],v_pixels=js["v_pixels"]))
    elif component_type == 'TabGroup':
            components.append(sg.TabGroup(layout=js["layout"],tab_location=js["tab_location"],title_color=js["title_color"],tab_background_color=js["tab_background_color"],selected_title_color=js["selected_title_color"],selected_background_color=js["selected_background_color"],background_color=js["background_color"],focus_color=js["focus_color"],font=js["font"],change_submits=js["change_submits"],enable_events=js["enable_events"],pad=js["pad"],p=js["p"],border_width=js["border_width"],tab_border_width=js["tab_border_width"],theme=js["theme"],key=js["key"],k=js["k"],size=js["size"],s=js["s"],tooltip=js["tooltip"],right_click_menu=js["right_click_menu"],expand_x=js["expand_x"],expand_y=js["expand_y"],visible=js["visible"],metadata=js["metadata"]))
    elif component_type == 'obj_to_string':
            components.append(sg.obj_to_string(obj=js["obj"],extra=js["extra"]))
    elif component_type == 'Graph':
            components.append(sg.Graph(canvas_size=js["canvas_size"],graph_bottom_left=js["graph_bottom_left"],graph_top_right=js["graph_top_right"],background_color=js["background_color"],pad=js["pad"],p=js["p"],change_submits=js["change_submits"],drag_submits=js["drag_submits"],enable_events=js["enable_events"],motion_events=js["motion_events"],key=js["key"],k=js["k"],tooltip=js["tooltip"],right_click_menu=js["right_click_menu"],expand_x=js["expand_x"],expand_y=js["expand_y"],visible=js["visible"],float_values=js["float_values"],border_width=js["border_width"],metadata=js["metadata"]))
    elif component_type == 'cprint':
            components.append(sg.cprint(args=js["*args"],text_color=js["text_color"],font=js["font"],background_color=js["background_color"],colors=js["colors"],t=js["t"],b=js["b"],c=js["c"],end=js["end"],sep=js["sep"],key=js["key"],window=js["window"],justification=js["justification"],autoscroll=js["autoscroll"],multiline_key=js["multiline_key"]))
    elif component_type == 'FillFormWithValues':
            components.append(sg.FillFormWithValues(window=js["window"],values_dict=js["values_dict"]))
    elif component_type == 'TreeData':
            components.append(sg.TreeData())
    elif component_type == 'Titlebar':
            components.append(sg.Titlebar(icon=js["icon"],title=js["title"],text_color=js["text_color"],background_color=js["background_color"],font=js["font"],key=js["key"],k=js["k"]))
    elif component_type == 'Radio':
            components.append(sg.Radio(text=js["text"],group_id=js["group_id"],default=js["default"],disabled=js["disabled"],size=js["size"],s=js["s"],auto_size_text=js["auto_size_text"],background_color=js["background_color"],text_color=js["text_color"],circle_color=js["circle_color"],font=js["font"],key=js["key"],k=js["k"],pad=js["pad"],p=js["p"],tooltip=js["tooltip"],change_submits=js["change_submits"],enable_events=js["enable_events"],right_click_menu=js["right_click_menu"],expand_x=js["expand_x"],expand_y=js["expand_y"],visible=js["visible"],metadata=js["metadata"]))
    elif component_type == 'Button':
            components.append(sg.Button(button_text=js["button_text"],button_type=js["button_type"],target=js["target"],tooltip=js["tooltip"],file_types=js["file_types"],initial_folder=js["initial_folder"],default_extension=js["default_extension"],disabled=js["disabled"],change_submits=js["change_submits"],enable_events=js["enable_events"],image_source=js["image_source"],image_filename=js["image_filename"],image_data=js["image_data"],image_size=js["image_size"],image_subsample=js["image_subsample"],image_zoom=js["image_zoom"],border_width=js["border_width"],size=js["size"],s=js["s"],auto_size_button=js["auto_size_button"],button_color=js["button_color"],disabled_button_color=js["disabled_button_color"],highlight_colors=js["highlight_colors"],mouseover_colors=js["mouseover_colors"],use_ttk_buttons=js["use_ttk_buttons"],font=js["font"],bind_return_key=js["bind_return_key"],focus=js["focus"],pad=js["pad"],p=js["p"],key=js["key"],k=js["k"],right_click_menu=js["right_click_menu"],expand_x=js["expand_x"],expand_y=js["expand_y"],visible=js["visible"],metadata=js["metadata"]))
    elif component_type == 'ProgressBar':
            components.append(sg.ProgressBar(max_value=js["max_value"],orientation=js["orientation"],size=js["size"],s=js["s"],size_px=js["size_px"],auto_size_text=js["auto_size_text"],bar_color=js["bar_color"],style=js["style"],border_width=js["border_width"],relief=js["relief"],key=js["key"],k=js["k"],pad=js["pad"],p=js["p"],right_click_menu=js["right_click_menu"],expand_x=js["expand_x"],expand_y=js["expand_y"],visible=js["visible"],metadata=js["metadata"]))
    elif component_type == 'VerticalSeparator':
            components.append(sg.VerticalSeparator(color=js["color"],pad=js["pad"],p=js["p"],key=js["key"],k=js["k"]))
    elif component_type == 'Tab':
            components.append(sg.Tab(title=js["title"],layout=js["layout"],title_color=js["title_color"],background_color=js["background_color"],font=js["font"],pad=js["pad"],p=js["p"],disabled=js["disabled"],border_width=js["border_width"],key=js["key"],k=js["k"],tooltip=js["tooltip"],right_click_menu=js["right_click_menu"],expand_x=js["expand_x"],expand_y=js["expand_y"],visible=js["visible"],element_justification=js["element_justification"],image_source=js["image_source"],image_subsample=js["image_subsample"],image_zoom=js["image_zoom"],metadata=js["metadata"]))
    elif component_type == 'Slider':
            components.append(sg.Slider(range=js["range"],default_value=js["default_value"],resolution=js["resolution"],tick_interval=js["tick_interval"],orientation=js["orientation"],disable_number_display=js["disable_number_display"],border_width=js["border_width"],relief=js["relief"],change_submits=js["change_submits"],enable_events=js["enable_events"],disabled=js["disabled"],size=js["size"],s=js["s"],font=js["font"],background_color=js["background_color"],text_color=js["text_color"],trough_color=js["trough_color"],key=js["key"],k=js["k"],pad=js["pad"],p=js["p"],expand_x=js["expand_x"],expand_y=js["expand_y"],tooltip=js["tooltip"],visible=js["visible"],metadata=js["metadata"]))
    return components
def new_win(layout):
    window = sg.Window('Layout Designer', [convert_layout_to_components(layout)], finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Generate Layout':
            generated_layout = [component for component in components_on_canvas.values()]
            print('Generated layout:', generated_layout)
            new_win(generated_layout)
            break
def get_num_list():
    return '1,2,3,4,5,6,7,8,9'.split(',')
def is_str(obj):
    if type(obj) is str:
        return True
def is_int(obj):
    if type(obj) is int:
        return True
def is_float(obj):
    if type(obj) is float:
        return True
def make_str(obj):
    if is_str(obj):
        return obj
    return str(obj)
def is_number(obj):
    if is_int(obj):
        return True
    if is_float(obj):
        return True
    obj = make_str(obj)
    num_ls = get_num_list()
    for k in range(0,len(obj)):
        if obj[k] not in num_ls:
            return False
    return True
def get_type(obj):
    if is_number(obj):
        obj = int(obj)
    if is_float(obj):
        return float(obj)
    elif obj == 'None':
        obj =  None
    elif is_str(obj):
        obj =  str(obj)
    return obj
def layout_designer(components):
    canvas = sg.Graph(canvas_size=(800, 600),
                      graph_bottom_left=(0, 0),
                      graph_top_right=(800, 600),
                      background_color='white',
                      key='canvas',
                      enable_events=True,
                      drag_submits=True)

    component_list = sg.Listbox(values=components,
                                size=(20, 20),
                                key='-COMPONENTS-',
                                enable_events=True,
                                horizontal_scroll=True,
                                )

    layout = [
        [canvas],
        [component_list],
        [sg.Button('Generate Layout')],
 
    ]

    window = sg.Window('Layout Designer', layout, finalize=True)
    canvas = window['canvas']

    selected_component = None
    components_on_canvas = {}

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Generate Layout':
            generated_layout = [component for component in components_on_canvas.values()]
            for component in generated_layout:
                if 'attributes' in component:
                    component.update(component['attributes'])
                    del component['attributes']
                    if 'size' in component:
                        if isinstance(component['size'], str) and component['size'] != '(None, None)':
                            component['size'] = tuple(map(int, component['size'][1:-1].split(', ')))
                        elif component['size'] == '(None, None)':
                            component['size'] = (None, None)
            print('Generated layout:', generated_layout)
            new_win(generated_layout)
            break
        if event == '-COMPONENTS-':
            selected_component = values['-COMPONENTS-'][0]
        if event == 'canvas':
            if selected_component:
                x, y = values['canvas']
                component_id = canvas.draw_rectangle(top_left=(x - 25, y - 12), bottom_right=(x + 25, y + 12), fill_color='#ddeeff', line_color='black', line_width=1)
                text_id = canvas.draw_text(selected_component, values['canvas'])
                components_on_canvas[component_id] = {
                    'component': selected_component,
                    'text_id': text_id,
                    'size': (50, 25)
                }

                if selected_component in input_list:
                    component_input_list = input_list[selected_component]["components"]
                    component_descriptions_list = input_list[selected_component]["descriptions"]
                    layout = []
                    for attr in component_input_list:
                        if is_tuple_attribute(component_input_list[attr]):
                            default_values = component_input_list[attr][1:-1].split(', ')
                            layout.append([
                                sg.Text(attr, size=(15, 1), tooltip=component_descriptions_list[attr]["Meaning"]),
                                sg.InputText(default_values[0], key=f'-{attr}-0', size=(10, 1), tooltip=component_descriptions_list[attr]["Meaning"]),
                                sg.InputText(default_values[1], key=f'-{attr}-1', size=(10, 1), tooltip=component_descriptions_list[attr]["Meaning"])
                            ])
                            
                        elif component_input_list[attr].lower() in ["true", "false"] or component_descriptions_list[attr]["Type"].lower() == "bool":
                            default_value = True if component_input_list[attr].lower() == "true" else False
                            layout.append([
                                sg.Text(attr, size=(15, 1), tooltip=component_descriptions_list[attr]["Meaning"]),
                                sg.Checkbox("", default=default_value, key=f'-{attr}-', tooltip=component_descriptions_list[attr]["Meaning"])
                            ])
                        elif 'color' in attr:
                            layout.append([
                                sg.Text(attr, size=(15, 1), tooltip=component_descriptions_list[attr]["Meaning"]),
                                sg.InputText(component_input_list[attr], key=f'-{attr}-', size=(20, 1), tooltip=component_descriptions_list[attr]["Meaning"]),
                                sg.ColorChooserButton('Color', key=f'-{attr}-picker', tooltip='Open color picker')
                            ])
                        else:
                            layout.append([
                                sg.Text(attr, size=(15, 1), tooltip=component_descriptions_list[attr]["Meaning"]),
                                sg.InputText(component_input_list[attr], key=f'-{attr}-', size=(20, 1), tooltip=component_descriptions_list[attr]["Meaning"])
                            ])
                    layout += [[sg.Button('Save'), sg.Button('Cancel')]]
                    attribute_window = sg.Window(f'Edit {selected_component} Attributes', layout)

                    while True:
                        sub_event, sub_values = attribute_window.read()
                        if sub_event in (sg.WIN_CLOSED, 'Cancel'):
                            break
                        elif sub_event.endswith('-picker'):
                            attr = sub_event[:-7]
                            color = sg.popup_get_color()
                            if color:
                                window[f'-{attr}-'].update(value=color)
                        if sub_event == 'Save':
                            attributes = {}
                            for attr in component_input_list:
                                if is_tuple_attribute(component_input_list[attr]):
                                    value0,value1 = sub_values[f'-{attr}-0'],sub_values[f'-{attr}-1']
                                    attributes[attr] = (get_type(value0), get_type(value1))
                                else:
                                    attributes[attr] = sub_values[f'-{attr}-']
                            
                            components_on_canvas[component_id]['attributes'] = attributes
                            attribute_window.close()
                            break

                    selected_component = None

        if event.startswith('canvas'):
            event_parts = event.split('+')
            if len(event_parts) < 2 or not event_parts[1].isdigit():
                continue  # Ignore the event if the second part is not an integer

            component_id = int(event_parts[1])
            if 'Hover' in event:
                canvas.TKCanvas.tag_raise(component_id)
                canvas.TKCanvas.tag_raise(components_on_canvas[component_id]['text_id'])

                attributes = components_on_canvas[component_id]
                hover_text = f"Component: {attributes['component']}\nSize: {attributes['size']}"
                window['canvas'].set_tooltip(hover_text)

            if 'Click' in event:
                attributes = components_on_canvas[component_id]
                current_size = attributes['size']
                layout = [
                    [sg.Text('Size:'), sg.InputText(current_size[0], key='-WIDTH-', size=(5, 1)), sg.InputText(current_size[1], key='-HEIGHT-', size=(5, 1))],
                    [sg.Button('Save'), sg.Button('Cancel')]
                ]
                attribute_window = sg.Window('Edit Component Attributes', layout)

                while True:
                    sub_event, sub_values = attribute_window.read()
                    if sub_event in (sg.WIN_CLOSED, 'Cancel'):
                        break
                    if sub_event == 'Save':
                        new_width = int(sub_values['-WIDTH-'])
                        new_height = int(sub_values['-HEIGHT-'])
                        components_on_canvas[component_id]['size'] = (new_width, new_height)

                        x, y = canvas.get_location(component_id)
                        canvas.delete_figure(component_id)
                        canvas.delete_figure(components_on_canvas[component_id]['text_id'])

                        new_component_id = canvas.draw_rectangle(top_left=(x - new_width // 2, y - new_height // 2), bottom_right=(x + new_width // 2, y + new_height // 2), fill_color='#ddeeff', line_color='black', line_width=1)
                        new_text_id = canvas.draw_text(components_on_canvas[component_id]['component'], (x, y))
                        components_on_canvas[new_component_id] = {
                            'component': components_on_canvas[component_id]['component'],
                            'text_id': new_text_id,
                            'size': (new_width, new_height)
                        }

                        canvas.delete_figure(component_id)
                        del components_on_canvas[component_id]

                        attribute_window.close()
                        break
def create_all_ifs():
    for k in range(0,len(components)):
        comp_now = input_list[components[k]]["components"]
        func = get_new_function(components[k])
        keys = list(comp_now.keys())
        for j in range(0,len(keys)):
            func = func+f'''{keys[j]}=js["{keys[j]}"],'''
        func = func + '))'
        print(func)
def get_new_function(name):
    return f'''elif component_type == '{name}':
        components.append(sg.{name}('''
global input_list
input_list = json.loads(reader('data/parse_html/js_total.json'))
input(input_list["Button"])
components = list(json.loads(reader('data/parse_html/js_total.json')).keys())
layout_designer(components)
