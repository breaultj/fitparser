# base_types
base_types = {
 0 :  { 'endian' : 0, 'type' : 'enum', 'invalid' : '0xFF', 'bytes' : 1},
 1 :  { 'endian' : 0, 'type' : 'sint8', 'invalid' : '0x7F', 'bytes' : 1},
 2 :  { 'endian' : 0, 'type' : 'unit8', 'invalid' : '0xFF', 'bytes' : 1},
 3 :  { 'endian' : 1, 'type' : 'sint16', 'invalid' : '0x7FFF', 'bytes' : 2},
 4 :  { 'endian' : 1, 'type' : 'uint16', 'invalid' : '0xFFFF', 'bytes' : 2},
 5 :  { 'endian' : 1, 'type' : 'sint32', 'invalid' : '0x7FFFFFFF', 'bytes' : 4},
 6 :  { 'endian' : 1, 'type' : 'uint32', 'invalid' : '0xFFFFFFFF', 'bytes' : 4},
 7 :  { 'endian' : 0, 'type' : 'string', 'invalid' : '0x00', 'bytes' : 1},
 8 :  { 'endian' : 1, 'type' : 'float32', 'invalid' : '0xFFFFFFFF', 'bytes' : 4},
 9 :  { 'endian' : 1, 'type' : 'float64', 'invalid' : '0xFF', 'bytes' : 8},
 10 : { 'endian' : 0, 'type' : 'uint8z', 'invalid' : '0x00', 'bytes' : 1},
 11 : { 'endian' : 1, 'type' : 'uint16z', 'invalid' : '0x0000', 'bytes' : 2},
 12 : { 'endian' : 1, 'type' : 'uint32z', 'invalid' : '0x00000000', 'bytes' : 4},
 13 : { 'endian' : 0, 'type' : 'byte', 'invalid' : '0xFF', 'bytes' : 1 },
 14 : { 'endian' : 1, 'type' : 'sint64', 'invalid' : '0xFF', 'bytes' : 8},
 15 : { 'endian' : 1, 'type' : 'uint64', 'invalid' : '0xFF', 'bytes' : 8},
 16 : { 'endian' : 1, 'type' : 'uint64z', 'invalid' : '0xFF', 'bytes' : 8}
}

def getBaseType(num):
    return base_types[num]["type"]

file_id = {
0: { "name":"type","type": "file"},
1: { "name":"manufacturer","type": "manufacturer"},
2: { "name":"product","type": "uint16"},
3: { "name":"serial_number","type": "uint32z"},
4: { "name":"time_created","type": "date_time"},
5: { "name":"number","type": "uint16"},
8: { "name":"product_name","type": "string"}
}

file_creator = {
0: { "name":"software_version","type": "uint16"},
1: { "name":"hardware_version","type": "uint8"}
}

timestamp_correlation = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"fractional_timestamp","type": "uint16"},
1: { "name":"system_timestamp","type": "date_time"},
2: { "name":"fractional_system_timestamp","type": "uint16"},
3: { "name":"local_timestamp","type": "local_date_time"},
4: { "name":"timestamp_ms","type": "uint16"},
5: { "name":"system_timestamp_ms","type": "uint16"}
}

software = {
254: { "name":"message_index","type": "message_index"},
3: { "name":"version","type": "uint16"},
5: { "name":"part_number","type": "string"}
}

slave_device = {
0: { "name":"manufacturer","type": "manufacturer"},
1: { "name":"product","type": "uint16"}
}

capabilities = {
0: { "name":"languages","type": "uint8z"},
1: { "name":"sports","type": "sport_bits_0"},
21: { "name":"workouts_supported","type": "workout_capabilities"},
23: { "name":"connectivity_supported","type": "connectivity_capabilities"}
}

file_capabilities = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"type","type": "file"},
1: { "name":"flags","type": "file_flags"},
2: { "name":"directory","type": "string"},
3: { "name":"max_count","type": "uint16"},
4: { "name":"max_size","type": "uint32"}
}

mesg_capabilities = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"file","type": "file"},
1: { "name":"mesg_num","type": "mesg_num"},
2: { "name":"count_type","type": "mesg_count"},
3: { "name":"count","type": "uint16"}
}

field_capabilities = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"file","type": "file"},
1: { "name":"mesg_num","type": "mesg_num"},
2: { "name":"field_num","type": "uint8"},
3: { "name":"count","type": "uint16"}
}

device_settings = {
0: { "name":"active_time_zone","type": "uint8"},
1: { "name":"utc_offset","type": "uint32"},
2: { "name":"time_offset","type": "uint32"},
4: { "name":"time_mode","type": "time_mode"},
5: { "name":"time_zone_offset","type": "sint8"},
12: { "name":"backlight_mode","type": "backlight_mode"},
36: { "name":"activity_tracker_enabled","type": "bool"},
39: { "name":"clock_time","type": "date_time"},
40: { "name":"pages_enabled","type": "uint16"},
46: { "name":"move_alert_enabled","type": "bool"},
47: { "name":"date_mode","type": "date_mode"},
55: { "name":"display_orientation","type": "display_orientation"},
56: { "name":"mounting_side","type": "side"},
57: { "name":"default_page","type": "uint16"},
58: { "name":"autosync_min_steps","type": "uint16"},
59: { "name":"autosync_min_time","type": "uint16"},
80: { "name":"lactate_threshold_autodetect_enabled","type": "bool"},
86: { "name":"ble_auto_upload_enabled","type": "bool"},
89: { "name":"auto_sync_frequency","type": "auto_sync_frequency"},
90: { "name":"auto_activity_detect","type": "auto_activity_detect"},
94: { "name":"number_of_screens","type": "uint8"},
95: { "name":"smart_notification_display_orientation","type": "display_orientation"},
134: { "name":"tap_interface","type": "switch"},
174: { "name":"tap_sensitivity","type": "tap_sensitivity"}
}

user_profile = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"friendly_name","type": "string"},
1: { "name":"gender","type": "gender"},
2: { "name":"age","type": "uint8"},
3: { "name":"height","type": "uint8"},
4: { "name":"weight","type": "uint16"},
5: { "name":"language","type": "language"},
6: { "name":"elev_setting","type": "display_measure"},
7: { "name":"weight_setting","type": "display_measure"},
8: { "name":"resting_heart_rate","type": "uint8"},
9: { "name":"default_max_running_heart_rate","type": "uint8"},
10: { "name":"default_max_biking_heart_rate","type": "uint8"},
11: { "name":"default_max_heart_rate","type": "uint8"},
12: { "name":"hr_setting","type": "display_heart"},
13: { "name":"speed_setting","type": "display_measure"},
14: { "name":"dist_setting","type": "display_measure"},
16: { "name":"power_setting","type": "display_power"},
17: { "name":"activity_class","type": "activity_class"},
18: { "name":"position_setting","type": "display_position"},
21: { "name":"temperature_setting","type": "display_measure"},
22: { "name":"local_id","type": "user_local_id"},
23: { "name":"global_id","type": "byte"},
28: { "name":"wake_time","type": "localtime_into_day"},
29: { "name":"sleep_time","type": "localtime_into_day"},
30: { "name":"height_setting","type": "display_measure"},
31: { "name":"user_running_step_length","type": "uint16"},
32: { "name":"user_walking_step_length","type": "uint16"},
47: { "name":"depth_setting","type": "display_measure"},
49: { "name":"dive_count","type": "uint32"}
}

hrm_profile = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"enabled","type": "bool"},
1: { "name":"hrm_ant_id","type": "uint16z"},
2: { "name":"log_hrv","type": "bool"},
3: { "name":"hrm_ant_id_trans_type","type": "uint8z"}
}

sdm_profile = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"enabled","type": "bool"},
1: { "name":"sdm_ant_id","type": "uint16z"},
2: { "name":"sdm_cal_factor","type": "uint16"},
3: { "name":"odometer","type": "uint32"},
4: { "name":"speed_source","type": "bool"},
5: { "name":"sdm_ant_id_trans_type","type": "uint8z"},
7: { "name":"odometer_rollover","type": "uint8"}
}

bike_profile = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"name","type": "string"},
1: { "name":"sport","type": "sport"},
2: { "name":"sub_sport","type": "sub_sport"},
3: { "name":"odometer","type": "uint32"},
4: { "name":"bike_spd_ant_id","type": "uint16z"},
5: { "name":"bike_cad_ant_id","type": "uint16z"},
6: { "name":"bike_spdcad_ant_id","type": "uint16z"},
7: { "name":"bike_power_ant_id","type": "uint16z"},
8: { "name":"custom_wheelsize","type": "uint16"},
9: { "name":"auto_wheelsize","type": "uint16"},
10: { "name":"bike_weight","type": "uint16"},
11: { "name":"power_cal_factor","type": "uint16"},
12: { "name":"auto_wheel_cal","type": "bool"},
13: { "name":"auto_power_zero","type": "bool"},
14: { "name":"id","type": "uint8"},
15: { "name":"spd_enabled","type": "bool"},
16: { "name":"cad_enabled","type": "bool"},
17: { "name":"spdcad_enabled","type": "bool"},
18: { "name":"power_enabled","type": "bool"},
19: { "name":"crank_length","type": "uint8"},
20: { "name":"enabled","type": "bool"},
21: { "name":"bike_spd_ant_id_trans_type","type": "uint8z"},
22: { "name":"bike_cad_ant_id_trans_type","type": "uint8z"},
23: { "name":"bike_spdcad_ant_id_trans_type","type": "uint8z"},
24: { "name":"bike_power_ant_id_trans_type","type": "uint8z"},
37: { "name":"odometer_rollover","type": "uint8"},
38: { "name":"front_gear_num","type": "uint8z"},
39: { "name":"front_gear","type": "uint8z"},
40: { "name":"rear_gear_num","type": "uint8z"},
41: { "name":"rear_gear","type": "uint8z"},
44: { "name":"shimano_di2_enabled","type": "bool"}
}

connectivity = {
0: { "name":"bluetooth_enabled","type": "bool"},
1: { "name":"bluetooth_le_enabled","type": "bool"},
2: { "name":"ant_enabled","type": "bool"},
3: { "name":"name","type": "string"},
4: { "name":"live_tracking_enabled","type": "bool"},
5: { "name":"weather_conditions_enabled","type": "bool"},
6: { "name":"weather_alerts_enabled","type": "bool"},
7: { "name":"auto_activity_upload_enabled","type": "bool"},
8: { "name":"course_download_enabled","type": "bool"},
9: { "name":"workout_download_enabled","type": "bool"},
10: { "name":"gps_ephemeris_download_enabled","type": "bool"},
11: { "name":"incident_detection_enabled","type": "bool"},
12: { "name":"grouptrack_enabled","type": "bool"}
}

watchface_settings = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"mode","type": "watchface_mode"},
1: { "name":"layout","type": "byte"}
}

ohr_settings = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"enabled","type": "switch"}
}

zones_target = {
1: { "name":"max_heart_rate","type": "uint8"},
2: { "name":"threshold_heart_rate","type": "uint8"},
3: { "name":"functional_threshold_power","type": "uint16"},
5: { "name":"hr_calc_type","type": "hr_zone_calc"},
7: { "name":"pwr_calc_type","type": "pwr_zone_calc"}
}

sport = {
0: { "name":"sport","type": "sport"},
1: { "name":"sub_sport","type": "sub_sport"},
3: { "name":"name","type": "string"}
}

hr_zone = {
254: { "name":"message_index","type": "message_index"},
1: { "name":"high_bpm","type": "uint8"},
2: { "name":"name","type": "string"}
}

speed_zone = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"high_value","type": "uint16"},
1: { "name":"name","type": "string"}
}

cadence_zone = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"high_value","type": "uint8"},
1: { "name":"name","type": "string"}
}

power_zone = {
254: { "name":"message_index","type": "message_index"},
1: { "name":"high_value","type": "uint16"},
2: { "name":"name","type": "string"}
}

met_zone = {
254: { "name":"message_index","type": "message_index"},
1: { "name":"high_bpm","type": "uint8"},
2: { "name":"calories","type": "uint16"},
3: { "name":"fat_calories","type": "uint8"}
}

dive_settings = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"name","type": "string"},
1: { "name":"model","type": "tissue_model_type"},
2: { "name":"gf_low","type": "uint8"},
3: { "name":"gf_high","type": "uint8"},
4: { "name":"water_type","type": "water_type"},
5: { "name":"water_density","type": "float32"},
6: { "name":"po2_warn","type": "uint8"},
7: { "name":"po2_critical","type": "uint8"},
8: { "name":"po2_deco","type": "uint8"},
9: { "name":"safety_stop_enabled","type": "bool"},
10: { "name":"bottom_depth","type": "float32"},
11: { "name":"bottom_time","type": "uint32"},
12: { "name":"apnea_countdown_enabled","type": "bool"},
13: { "name":"apnea_countdown_time","type": "uint32"},
14: { "name":"backlight_mode","type": "dive_backlight_mode"},
15: { "name":"backlight_brightness","type": "uint8"},
16: { "name":"backlight_timeout","type": "backlight_timeout"},
17: { "name":"repeat_dive_interval","type": "uint16"},
18: { "name":"safety_stop_time","type": "uint16"},
19: { "name":"heart_rate_source_type","type": "source_type"},
20: { "name":"heart_rate_source","type": "uint8"}
}

dive_alarm = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"depth","type": "uint32"},
1: { "name":"time","type": "sint32"},
2: { "name":"enabled","type": "bool"},
3: { "name":"alarm_type","type": "dive_alarm_type"},
4: { "name":"sound","type": "tone"},
5: { "name":"dive_types","type": "sub_sport"}
}

dive_gas = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"helium_content","type": "uint8"},
1: { "name":"oxygen_content","type": "uint8"},
2: { "name":"status","type": "dive_gas_status"}
}

goal = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"sport","type": "sport"},
1: { "name":"sub_sport","type": "sub_sport"},
2: { "name":"start_date","type": "date_time"},
3: { "name":"end_date","type": "date_time"},
4: { "name":"type","type": "goal"},
5: { "name":"value","type": "uint32"},
6: { "name":"repeat","type": "bool"},
7: { "name":"target_value","type": "uint32"},
8: { "name":"recurrence","type": "goal_recurrence"},
9: { "name":"recurrence_value","type": "uint16"},
10: { "name":"enabled","type": "bool"},
11: { "name":"source","type": "goal_source"}
}

activity = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"total_timer_time","type": "uint32"},
1: { "name":"num_sessions","type": "uint16"},
2: { "name":"type","type": "activity"},
3: { "name":"event","type": "event"},
4: { "name":"event_type","type": "event_type"},
5: { "name":"local_timestamp","type": "local_date_time"},
6: { "name":"event_group","type": "uint8"}
}

session = {
254: { "name":"message_index","type": "message_index"},
253: { "name":"timestamp","type": "date_time"},
0: { "name":"event","type": "event"},
1: { "name":"event_type","type": "event_type"},
2: { "name":"start_time","type": "date_time"},
3: { "name":"start_position_lat","type": "sint32"},
4: { "name":"start_position_long","type": "sint32"},
5: { "name":"sport","type": "sport"},
6: { "name":"sub_sport","type": "sub_sport"},
7: { "name":"total_elapsed_time","type": "uint32"},
8: { "name":"total_timer_time","type": "uint32"},
9: { "name":"total_distance","type": "uint32"},
10: { "name":"total_cycles","type": "uint32"},
11: { "name":"total_calories","type": "uint16"},
13: { "name":"total_fat_calories","type": "uint16"},
14: { "name":"avg_speed","type": "uint16"},
15: { "name":"max_speed","type": "uint16"},
16: { "name":"avg_heart_rate","type": "uint8"},
17: { "name":"max_heart_rate","type": "uint8"},
18: { "name":"avg_cadence","type": "uint8"},
19: { "name":"max_cadence","type": "uint8"},
20: { "name":"avg_power","type": "uint16"},
21: { "name":"max_power","type": "uint16"},
22: { "name":"total_ascent","type": "uint16"},
23: { "name":"total_descent","type": "uint16"},
24: { "name":"total_training_effect","type": "uint8"},
25: { "name":"first_lap_index","type": "uint16"},
26: { "name":"num_laps","type": "uint16"},
27: { "name":"event_group","type": "uint8"},
28: { "name":"trigger","type": "session_trigger"},
29: { "name":"nec_lat","type": "sint32"},
30: { "name":"nec_long","type": "sint32"},
31: { "name":"swc_lat","type": "sint32"},
32: { "name":"swc_long","type": "sint32"},
34: { "name":"normalized_power","type": "uint16"},
35: { "name":"training_stress_score","type": "uint16"},
36: { "name":"intensity_factor","type": "uint16"},
37: { "name":"left_right_balance","type": "left_right_balance_100"},
41: { "name":"avg_stroke_count","type": "uint32"},
42: { "name":"avg_stroke_distance","type": "uint16"},
43: { "name":"swim_stroke","type": "swim_stroke"},
44: { "name":"pool_length","type": "uint16"},
45: { "name":"threshold_power","type": "uint16"},
46: { "name":"pool_length_unit","type": "display_measure"},
47: { "name":"num_active_lengths","type": "uint16"},
48: { "name":"total_work","type": "uint32"},
49: { "name":"avg_altitude","type": "uint16"},
50: { "name":"max_altitude","type": "uint16"},
51: { "name":"gps_accuracy","type": "uint8"},
52: { "name":"avg_grade","type": "sint16"},
53: { "name":"avg_pos_grade","type": "sint16"},
54: { "name":"avg_neg_grade","type": "sint16"},
55: { "name":"max_pos_grade","type": "sint16"},
56: { "name":"max_neg_grade","type": "sint16"},
57: { "name":"avg_temperature","type": "sint8"},
58: { "name":"max_temperature","type": "sint8"},
59: { "name":"total_moving_time","type": "uint32"},
60: { "name":"avg_pos_vertical_speed","type": "sint16"},
61: { "name":"avg_neg_vertical_speed","type": "sint16"},
62: { "name":"max_pos_vertical_speed","type": "sint16"},
63: { "name":"max_neg_vertical_speed","type": "sint16"},
64: { "name":"min_heart_rate","type": "uint8"},
65: { "name":"time_in_hr_zone","type": "uint32"},
66: { "name":"time_in_speed_zone","type": "uint32"},
67: { "name":"time_in_cadence_zone","type": "uint32"},
68: { "name":"time_in_power_zone","type": "uint32"},
69: { "name":"avg_lap_time","type": "uint32"},
70: { "name":"best_lap_index","type": "uint16"},
71: { "name":"min_altitude","type": "uint16"},
82: { "name":"player_score","type": "uint16"},
83: { "name":"opponent_score","type": "uint16"},
84: { "name":"opponent_name","type": "string"},
85: { "name":"stroke_count","type": "uint16"},
86: { "name":"zone_count","type": "uint16"},
87: { "name":"max_ball_speed","type": "uint16"},
88: { "name":"avg_ball_speed","type": "uint16"},
89: { "name":"avg_vertical_oscillation","type": "uint16"},
90: { "name":"avg_stance_time_percent","type": "uint16"},
91: { "name":"avg_stance_time","type": "uint16"},
92: { "name":"avg_fractional_cadence","type": "uint8"},
93: { "name":"max_fractional_cadence","type": "uint8"},
94: { "name":"total_fractional_cycles","type": "uint8"},
95: { "name":"avg_total_hemoglobin_conc","type": "uint16"},
96: { "name":"min_total_hemoglobin_conc","type": "uint16"},
97: { "name":"max_total_hemoglobin_conc","type": "uint16"},
98: { "name":"avg_saturated_hemoglobin_percent","type": "uint16"},
99: { "name":"min_saturated_hemoglobin_percent","type": "uint16"},
100: { "name":"max_saturated_hemoglobin_percent","type": "uint16"},
101: { "name":"avg_left_torque_effectiveness","type": "uint8"},
102: { "name":"avg_right_torque_effectiveness","type": "uint8"},
103: { "name":"avg_left_pedal_smoothness","type": "uint8"},
104: { "name":"avg_right_pedal_smoothness","type": "uint8"},
105: { "name":"avg_combined_pedal_smoothness","type": "uint8"},
111: { "name":"sport_index","type": "uint8"},
112: { "name":"time_standing","type": "uint32"},
113: { "name":"stand_count","type": "uint16"},
114: { "name":"avg_left_pco","type": "sint8"},
115: { "name":"avg_right_pco","type": "sint8"},
116: { "name":"avg_left_power_phase","type": "uint8"},
117: { "name":"avg_left_power_phase_peak","type": "uint8"},
118: { "name":"avg_right_power_phase","type": "uint8"},
119: { "name":"avg_right_power_phase_peak","type": "uint8"},
120: { "name":"avg_power_position","type": "uint16"},
121: { "name":"max_power_position","type": "uint16"},
122: { "name":"avg_cadence_position","type": "uint8"},
123: { "name":"max_cadence_position","type": "uint8"},
124: { "name":"enhanced_avg_speed","type": "uint32"},
125: { "name":"enhanced_max_speed","type": "uint32"},
126: { "name":"enhanced_avg_altitude","type": "uint32"},
127: { "name":"enhanced_min_altitude","type": "uint32"},
128: { "name":"enhanced_max_altitude","type": "uint32"},
129: { "name":"avg_lev_motor_power","type": "uint16"},
130: { "name":"max_lev_motor_power","type": "uint16"},
131: { "name":"lev_battery_consumption","type": "uint8"},
132: { "name":"avg_vertical_ratio","type": "uint16"},
133: { "name":"avg_stance_time_balance","type": "uint16"},
134: { "name":"avg_step_length","type": "uint16"},
137: { "name":"total_anaerobic_training_effect","type": "uint8"},
139: { "name":"avg_vam","type": "uint16"},
181: { "name":"total_grit","type": "float32"},
182: { "name":"total_flow","type": "float32"},
183: { "name":"jump_count","type": "uint16"},
186: { "name":"avg_grit","type": "float32"},
187: { "name":"avg_flow","type": "float32"}
}

lap = {
254: { "name":"message_index","type": "message_index"},
253: { "name":"timestamp","type": "date_time"},
0: { "name":"event","type": "event"},
1: { "name":"event_type","type": "event_type"},
2: { "name":"start_time","type": "date_time"},
3: { "name":"start_position_lat","type": "sint32"},
4: { "name":"start_position_long","type": "sint32"},
5: { "name":"end_position_lat","type": "sint32"},
6: { "name":"end_position_long","type": "sint32"},
7: { "name":"total_elapsed_time","type": "uint32"},
8: { "name":"total_timer_time","type": "uint32"},
9: { "name":"total_distance","type": "uint32"},
10: { "name":"total_cycles","type": "uint32"},
11: { "name":"total_calories","type": "uint16"},
12: { "name":"total_fat_calories","type": "uint16"},
13: { "name":"avg_speed","type": "uint16"},
14: { "name":"max_speed","type": "uint16"},
15: { "name":"avg_heart_rate","type": "uint8"},
16: { "name":"max_heart_rate","type": "uint8"},
17: { "name":"avg_cadence","type": "uint8"},
18: { "name":"max_cadence","type": "uint8"},
19: { "name":"avg_power","type": "uint16"},
20: { "name":"max_power","type": "uint16"},
21: { "name":"total_ascent","type": "uint16"},
22: { "name":"total_descent","type": "uint16"},
23: { "name":"intensity","type": "intensity"},
24: { "name":"lap_trigger","type": "lap_trigger"},
25: { "name":"sport","type": "sport"},
26: { "name":"event_group","type": "uint8"},
32: { "name":"num_lengths","type": "uint16"},
33: { "name":"normalized_power","type": "uint16"},
34: { "name":"left_right_balance","type": "left_right_balance_100"},
35: { "name":"first_length_index","type": "uint16"},
37: { "name":"avg_stroke_distance","type": "uint16"},
38: { "name":"swim_stroke","type": "swim_stroke"},
39: { "name":"sub_sport","type": "sub_sport"},
40: { "name":"num_active_lengths","type": "uint16"},
41: { "name":"total_work","type": "uint32"},
42: { "name":"avg_altitude","type": "uint16"},
43: { "name":"max_altitude","type": "uint16"},
44: { "name":"gps_accuracy","type": "uint8"},
45: { "name":"avg_grade","type": "sint16"},
46: { "name":"avg_pos_grade","type": "sint16"},
47: { "name":"avg_neg_grade","type": "sint16"},
48: { "name":"max_pos_grade","type": "sint16"},
49: { "name":"max_neg_grade","type": "sint16"},
50: { "name":"avg_temperature","type": "sint8"},
51: { "name":"max_temperature","type": "sint8"},
52: { "name":"total_moving_time","type": "uint32"},
53: { "name":"avg_pos_vertical_speed","type": "sint16"},
54: { "name":"avg_neg_vertical_speed","type": "sint16"},
55: { "name":"max_pos_vertical_speed","type": "sint16"},
56: { "name":"max_neg_vertical_speed","type": "sint16"},
57: { "name":"time_in_hr_zone","type": "uint32"},
58: { "name":"time_in_speed_zone","type": "uint32"},
59: { "name":"time_in_cadence_zone","type": "uint32"},
60: { "name":"time_in_power_zone","type": "uint32"},
61: { "name":"repetition_num","type": "uint16"},
62: { "name":"min_altitude","type": "uint16"},
63: { "name":"min_heart_rate","type": "uint8"},
71: { "name":"wkt_step_index","type": "message_index"},
74: { "name":"opponent_score","type": "uint16"},
75: { "name":"stroke_count","type": "uint16"},
76: { "name":"zone_count","type": "uint16"},
77: { "name":"avg_vertical_oscillation","type": "uint16"},
78: { "name":"avg_stance_time_percent","type": "uint16"},
79: { "name":"avg_stance_time","type": "uint16"},
80: { "name":"avg_fractional_cadence","type": "uint8"},
81: { "name":"max_fractional_cadence","type": "uint8"},
82: { "name":"total_fractional_cycles","type": "uint8"},
83: { "name":"player_score","type": "uint16"},
84: { "name":"avg_total_hemoglobin_conc","type": "uint16"},
85: { "name":"min_total_hemoglobin_conc","type": "uint16"},
86: { "name":"max_total_hemoglobin_conc","type": "uint16"},
87: { "name":"avg_saturated_hemoglobin_percent","type": "uint16"},
88: { "name":"min_saturated_hemoglobin_percent","type": "uint16"},
89: { "name":"max_saturated_hemoglobin_percent","type": "uint16"},
91: { "name":"avg_left_torque_effectiveness","type": "uint8"},
92: { "name":"avg_right_torque_effectiveness","type": "uint8"},
93: { "name":"avg_left_pedal_smoothness","type": "uint8"},
94: { "name":"avg_right_pedal_smoothness","type": "uint8"},
95: { "name":"avg_combined_pedal_smoothness","type": "uint8"},
98: { "name":"time_standing","type": "uint32"},
99: { "name":"stand_count","type": "uint16"},
100: { "name":"avg_left_pco","type": "sint8"},
101: { "name":"avg_right_pco","type": "sint8"},
102: { "name":"avg_left_power_phase","type": "uint8"},
103: { "name":"avg_left_power_phase_peak","type": "uint8"},
104: { "name":"avg_right_power_phase","type": "uint8"},
105: { "name":"avg_right_power_phase_peak","type": "uint8"},
106: { "name":"avg_power_position","type": "uint16"},
107: { "name":"max_power_position","type": "uint16"},
108: { "name":"avg_cadence_position","type": "uint8"},
109: { "name":"max_cadence_position","type": "uint8"},
110: { "name":"enhanced_avg_speed","type": "uint32"},
111: { "name":"enhanced_max_speed","type": "uint32"},
112: { "name":"enhanced_avg_altitude","type": "uint32"},
113: { "name":"enhanced_min_altitude","type": "uint32"},
114: { "name":"enhanced_max_altitude","type": "uint32"},
115: { "name":"avg_lev_motor_power","type": "uint16"},
116: { "name":"max_lev_motor_power","type": "uint16"},
117: { "name":"lev_battery_consumption","type": "uint8"},
118: { "name":"avg_vertical_ratio","type": "uint16"},
119: { "name":"avg_stance_time_balance","type": "uint16"},
120: { "name":"avg_step_length","type": "uint16"},
121: { "name":"avg_vam","type": "uint16"},
149: { "name":"total_grit","type": "float32"},
150: { "name":"total_flow","type": "float32"},
151: { "name":"jump_count","type": "uint16"},
153: { "name":"avg_grit","type": "float32"},
154: { "name":"avg_flow","type": "float32"}
}

length = {
254: { "name":"message_index","type": "message_index"},
253: { "name":"timestamp","type": "date_time"},
0: { "name":"event","type": "event"},
1: { "name":"event_type","type": "event_type"},
2: { "name":"start_time","type": "date_time"},
3: { "name":"total_elapsed_time","type": "uint32"},
4: { "name":"total_timer_time","type": "uint32"},
5: { "name":"total_strokes","type": "uint16"},
6: { "name":"avg_speed","type": "uint16"},
7: { "name":"swim_stroke","type": "swim_stroke"},
9: { "name":"avg_swimming_cadence","type": "uint8"},
10: { "name":"event_group","type": "uint8"},
11: { "name":"total_calories","type": "uint16"},
12: { "name":"length_type","type": "length_type"},
18: { "name":"player_score","type": "uint16"},
19: { "name":"opponent_score","type": "uint16"},
20: { "name":"stroke_count","type": "uint16"},
21: { "name":"zone_count","type": "uint16"}
}

record = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"position_lat","type": "sint32"},
1: { "name":"position_long","type": "sint32"},
2: { "name":"altitude","type": "uint16"},
3: { "name":"heart_rate","type": "uint8"},
4: { "name":"cadence","type": "uint8"},
5: { "name":"distance","type": "uint32"},
6: { "name":"speed","type": "uint16"},
7: { "name":"power","type": "uint16"},
8: { "name":"compressed_speed_distance","type": "byte"},
9: { "name":"grade","type": "sint16"},
10: { "name":"resistance","type": "uint8"},
11: { "name":"time_from_course","type": "sint32"},
12: { "name":"cycle_length","type": "uint8"},
13: { "name":"temperature","type": "sint8"},
17: { "name":"speed_1s","type": "uint8"},
18: { "name":"cycles","type": "uint8"},
19: { "name":"total_cycles","type": "uint32"},
28: { "name":"compressed_accumulated_power","type": "uint16"},
29: { "name":"accumulated_power","type": "uint32"},
30: { "name":"left_right_balance","type": "left_right_balance"},
31: { "name":"gps_accuracy","type": "uint8"},
32: { "name":"vertical_speed","type": "sint16"},
33: { "name":"calories","type": "uint16"},
39: { "name":"vertical_oscillation","type": "uint16"},
40: { "name":"stance_time_percent","type": "uint16"},
41: { "name":"stance_time","type": "uint16"},
42: { "name":"activity_type","type": "activity_type"},
43: { "name":"left_torque_effectiveness","type": "uint8"},
44: { "name":"right_torque_effectiveness","type": "uint8"},
45: { "name":"left_pedal_smoothness","type": "uint8"},
46: { "name":"right_pedal_smoothness","type": "uint8"},
47: { "name":"combined_pedal_smoothness","type": "uint8"},
48: { "name":"time128","type": "uint8"},
49: { "name":"stroke_type","type": "stroke_type"},
50: { "name":"zone","type": "uint8"},
51: { "name":"ball_speed","type": "uint16"},
52: { "name":"cadence256","type": "uint16"},
53: { "name":"fractional_cadence","type": "uint8"},
54: { "name":"total_hemoglobin_conc","type": "uint16"},
55: { "name":"total_hemoglobin_conc_min","type": "uint16"},
56: { "name":"total_hemoglobin_conc_max","type": "uint16"},
57: { "name":"saturated_hemoglobin_percent","type": "uint16"},
58: { "name":"saturated_hemoglobin_percent_min","type": "uint16"},
59: { "name":"saturated_hemoglobin_percent_max","type": "uint16"},
62: { "name":"device_index","type": "device_index"},
67: { "name":"left_pco","type": "sint8"},
68: { "name":"right_pco","type": "sint8"},
69: { "name":"left_power_phase","type": "uint8"},
70: { "name":"left_power_phase_peak","type": "uint8"},
71: { "name":"right_power_phase","type": "uint8"},
72: { "name":"right_power_phase_peak","type": "uint8"},
73: { "name":"enhanced_speed","type": "uint32"},
78: { "name":"enhanced_altitude","type": "uint32"},
81: { "name":"battery_soc","type": "uint8"},
82: { "name":"motor_power","type": "uint16"},
83: { "name":"vertical_ratio","type": "uint16"},
84: { "name":"stance_time_balance","type": "uint16"},
85: { "name":"step_length","type": "uint16"},
91: { "name":"absolute_pressure","type": "uint32"},
92: { "name":"depth","type": "uint32"},
93: { "name":"next_stop_depth","type": "uint32"},
94: { "name":"next_stop_time","type": "uint32"},
95: { "name":"time_to_surface","type": "uint32"},
96: { "name":"ndl_time","type": "uint32"},
97: { "name":"cns_load","type": "uint8"},
98: { "name":"n2_load","type": "uint16"},
114: { "name":"grit","type": "float32"},
115: { "name":"flow","type": "float32"},
117: { "name":"ebike_travel_range","type": "uint16"},
118: { "name":"ebike_battery_level","type": "uint8"},
119: { "name":"ebike_assist_mode","type": "uint8"},
120: { "name":"ebike_assist_level_percent","type": "uint8"}
}

event = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"event","type": "event"},
1: { "name":"event_type","type": "event_type"},
2: { "name":"data16","type": "uint16"},
3: { "name":"data","type": "uint32"},
4: { "name":"event_group","type": "uint8"},
7: { "name":"score","type": "uint16"},
8: { "name":"opponent_score","type": "uint16"},
9: { "name":"front_gear_num","type": "uint8z"},
10: { "name":"front_gear","type": "uint8z"},
11: { "name":"rear_gear_num","type": "uint8z"},
12: { "name":"rear_gear","type": "uint8z"},
13: { "name":"device_index","type": "device_index"}
}

device_info = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"device_index","type": "device_index"},
1: { "name":"device_type","type": "uint8"},
2: { "name":"manufacturer","type": "manufacturer"},
3: { "name":"serial_number","type": "uint32z"},
4: { "name":"product","type": "uint16"},
5: { "name":"software_version","type": "uint16"},
6: { "name":"hardware_version","type": "uint8"},
7: { "name":"cum_operating_time","type": "uint32"},
10: { "name":"battery_voltage","type": "uint16"},
11: { "name":"battery_status","type": "battery_status"},
18: { "name":"sensor_position","type": "body_location"},
19: { "name":"descriptor","type": "string"},
20: { "name":"ant_transmission_type","type": "uint8z"},
21: { "name":"ant_device_number","type": "uint16z"},
22: { "name":"ant_network","type": "ant_network"},
25: { "name":"source_type","type": "source_type"},
27: { "name":"product_name","type": "string"}
}

training_file = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"type","type": "file"},
1: { "name":"manufacturer","type": "manufacturer"},
2: { "name":"product","type": "uint16"},
3: { "name":"serial_number","type": "uint32z"},
4: { "name":"time_created","type": "date_time"}
}

hrv = {
0: { "name":"time","type": "uint16"}
}

weather_conditions = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"weather_report","type": "weather_report"},
1: { "name":"temperature","type": "sint8"},
2: { "name":"condition","type": "weather_status"},
3: { "name":"wind_direction","type": "uint16"},
4: { "name":"wind_speed","type": "uint16"},
5: { "name":"precipitation_probability","type": "uint8"},
6: { "name":"temperature_feels_like","type": "sint8"},
7: { "name":"relative_humidity","type": "uint8"},
8: { "name":"location","type": "string"},
9: { "name":"observed_at_time","type": "date_time"},
10: { "name":"observed_location_lat","type": "sint32"},
11: { "name":"observed_location_long","type": "sint32"},
12: { "name":"day_of_week","type": "day_of_week"},
13: { "name":"high_temperature","type": "sint8"},
14: { "name":"low_temperature","type": "sint8"}
}

weather_alert = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"report_id","type": "string"},
1: { "name":"issue_time","type": "date_time"},
2: { "name":"expire_time","type": "date_time"},
3: { "name":"severity","type": "weather_severity"},
4: { "name":"type","type": "weather_severe_type"}
}

gps_metadata = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"timestamp_ms","type": "uint16"},
1: { "name":"position_lat","type": "sint32"},
2: { "name":"position_long","type": "sint32"},
3: { "name":"enhanced_altitude","type": "uint32"},
4: { "name":"enhanced_speed","type": "uint32"},
5: { "name":"heading","type": "uint16"},
6: { "name":"utc_timestamp","type": "date_time"},
7: { "name":"velocity","type": "sint16"}
}

camera_event = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"timestamp_ms","type": "uint16"},
1: { "name":"camera_event_type","type": "camera_event_type"},
2: { "name":"camera_file_uuid","type": "string"},
3: { "name":"camera_orientation","type": "camera_orientation_type"}
}

gyroscope_data = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"timestamp_ms","type": "uint16"},
1: { "name":"sample_time_offset","type": "uint16"},
2: { "name":"gyro_x","type": "uint16"},
3: { "name":"gyro_y","type": "uint16"},
4: { "name":"gyro_z","type": "uint16"},
5: { "name":"calibrated_gyro_x","type": "float32"},
6: { "name":"calibrated_gyro_y","type": "float32"},
7: { "name":"calibrated_gyro_z","type": "float32"}
}

accelerometer_data = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"timestamp_ms","type": "uint16"},
1: { "name":"sample_time_offset","type": "uint16"},
2: { "name":"accel_x","type": "uint16"},
3: { "name":"accel_y","type": "uint16"},
4: { "name":"accel_z","type": "uint16"},
5: { "name":"calibrated_accel_x","type": "float32"},
6: { "name":"calibrated_accel_y","type": "float32"},
7: { "name":"calibrated_accel_z","type": "float32"},
8: { "name":"compressed_calibrated_accel_x","type": "sint16"},
9: { "name":"compressed_calibrated_accel_y","type": "sint16"},
10: { "name":"compressed_calibrated_accel_z","type": "sint16"}
}

magnetometer_data = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"timestamp_ms","type": "uint16"},
1: { "name":"sample_time_offset","type": "uint16"},
2: { "name":"mag_x","type": "uint16"},
3: { "name":"mag_y","type": "uint16"},
4: { "name":"mag_z","type": "uint16"},
5: { "name":"calibrated_mag_x","type": "float32"},
6: { "name":"calibrated_mag_y","type": "float32"},
7: { "name":"calibrated_mag_z","type": "float32"}
}

barometer_data = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"timestamp_ms","type": "uint16"},
1: { "name":"sample_time_offset","type": "uint16"},
2: { "name":"baro_pres","type": "uint32"}
}

three_d_sensor_calibration = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"sensor_type","type": "sensor_type"},
1: { "name":"calibration_factor","type": "uint32"},
2: { "name":"calibration_divisor","type": "uint32"},
3: { "name":"level_shift","type": "uint32"},
4: { "name":"offset_cal","type": "sint32"},
5: { "name":"orientation_matrix","type": "sint32"}
}

one_d_sensor_calibration = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"sensor_type","type": "sensor_type"},
1: { "name":"calibration_factor","type": "uint32"},
2: { "name":"calibration_divisor","type": "uint32"},
3: { "name":"level_shift","type": "uint32"},
4: { "name":"offset_cal","type": "sint32"}
}

video_frame = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"timestamp_ms","type": "uint16"},
1: { "name":"frame_number","type": "uint32"}
}

obdii_data = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"timestamp_ms","type": "uint16"},
1: { "name":"time_offset","type": "uint16"},
2: { "name":"pid","type": "byte"},
3: { "name":"raw_data","type": "byte"},
4: { "name":"pid_data_size","type": "uint8"},
5: { "name":"system_time","type": "uint32"},
6: { "name":"start_timestamp","type": "date_time"},
7: { "name":"start_timestamp_ms","type": "uint16"}
}

nmea_sentence = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"timestamp_ms","type": "uint16"},
1: { "name":"sentence","type": "string"}
}

aviation_attitude = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"timestamp_ms","type": "uint16"},
1: { "name":"system_time","type": "uint32"},
2: { "name":"pitch","type": "sint16"},
3: { "name":"roll","type": "sint16"},
4: { "name":"accel_lateral","type": "sint16"},
5: { "name":"accel_normal","type": "sint16"},
6: { "name":"turn_rate","type": "sint16"},
7: { "name":"stage","type": "attitude_stage"},
8: { "name":"attitude_stage_complete","type": "uint8"},
9: { "name":"track","type": "uint16"},
10: { "name":"validity","type": "attitude_validity"}
}

video = {
0: { "name":"url","type": "string"},
1: { "name":"hosting_provider","type": "string"},
2: { "name":"duration","type": "uint32"}
}

video_title = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"message_count","type": "uint16"},
1: { "name":"text","type": "string"}
}

video_description = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"message_count","type": "uint16"},
1: { "name":"text","type": "string"}
}

video_clip = {
0: { "name":"clip_number","type": "uint16"},
1: { "name":"start_timestamp","type": "date_time"},
2: { "name":"start_timestamp_ms","type": "uint16"},
3: { "name":"end_timestamp","type": "date_time"},
4: { "name":"end_timestamp_ms","type": "uint16"},
6: { "name":"clip_start","type": "uint32"},
7: { "name":"clip_end","type": "uint32"}
}

fit_set = {
254: { "name":"timestamp","type": "date_time"},
0: { "name":"duration","type": "uint32"},
3: { "name":"repetitions","type": "uint16"},
4: { "name":"weight","type": "uint16"},
5: { "name":"set_type","type": "set_type"},
6: { "name":"start_time","type": "date_time"},
7: { "name":"category","type": "exercise_category"},
8: { "name":"category_subtype","type": "uint16"},
9: { "name":"weight_display_unit","type": "fit_base_unit"},
10: { "name":"message_index","type": "message_index"},
11: { "name":"wkt_step_index","type": "message_index"}
}

jump = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"distance","type": "float32"},
1: { "name":"height","type": "float32"},
2: { "name":"rotations","type": "uint8"},
3: { "name":"hang_time","type": "float32"},
4: { "name":"score","type": "float32"},
5: { "name":"position_lat","type": "sint32"},
6: { "name":"position_long","type": "sint32"},
7: { "name":"speed","type": "uint16"},
8: { "name":"enhanced_speed","type": "uint32"}
}

course = {
4: { "name":"sport","type": "sport"},
5: { "name":"name","type": "string"},
6: { "name":"capabilities","type": "course_capabilities"},
7: { "name":"sub_sport","type": "sub_sport"}
}

course_point = {
254: { "name":"message_index","type": "message_index"},
1: { "name":"timestamp","type": "date_time"},
2: { "name":"position_lat","type": "sint32"},
3: { "name":"position_long","type": "sint32"},
4: { "name":"distance","type": "uint32"},
5: { "name":"type","type": "course_point"},
6: { "name":"name","type": "string"},
8: { "name":"favorite","type": "bool"}
}

segment_id = {
0: { "name":"name","type": "string"},
1: { "name":"uuid","type": "string"},
2: { "name":"sport","type": "sport"},
3: { "name":"enabled","type": "bool"},
4: { "name":"user_profile_primary_key","type": "uint32"},
5: { "name":"device_id","type": "uint32"},
6: { "name":"default_race_leader","type": "uint8"},
7: { "name":"delete_status","type": "segment_delete_status"},
8: { "name":"selection_type","type": "segment_selection_type"}
}

segment_leaderboard_entry = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"name","type": "string"},
1: { "name":"type","type": "segment_leaderboard_type"},
2: { "name":"group_primary_key","type": "uint32"},
3: { "name":"activity_id","type": "uint32"},
4: { "name":"segment_time","type": "uint32"},
5: { "name":"activity_id_string","type": "string"}
}

segment_point = {
254: { "name":"message_index","type": "message_index"},
1: { "name":"position_lat","type": "sint32"},
2: { "name":"position_long","type": "sint32"},
3: { "name":"distance","type": "uint32"},
4: { "name":"altitude","type": "uint16"},
5: { "name":"leader_time","type": "uint32"}
}

segment_lap = {
254: { "name":"message_index","type": "message_index"},
253: { "name":"timestamp","type": "date_time"},
0: { "name":"event","type": "event"},
1: { "name":"event_type","type": "event_type"},
2: { "name":"start_time","type": "date_time"},
3: { "name":"start_position_lat","type": "sint32"},
4: { "name":"start_position_long","type": "sint32"},
5: { "name":"end_position_lat","type": "sint32"},
6: { "name":"end_position_long","type": "sint32"},
7: { "name":"total_elapsed_time","type": "uint32"},
8: { "name":"total_timer_time","type": "uint32"},
9: { "name":"total_distance","type": "uint32"},
10: { "name":"total_cycles","type": "uint32"},
11: { "name":"total_calories","type": "uint16"},
12: { "name":"total_fat_calories","type": "uint16"},
13: { "name":"avg_speed","type": "uint16"},
14: { "name":"max_speed","type": "uint16"},
15: { "name":"avg_heart_rate","type": "uint8"},
16: { "name":"max_heart_rate","type": "uint8"},
17: { "name":"avg_cadence","type": "uint8"},
18: { "name":"max_cadence","type": "uint8"},
19: { "name":"avg_power","type": "uint16"},
20: { "name":"max_power","type": "uint16"},
21: { "name":"total_ascent","type": "uint16"},
22: { "name":"total_descent","type": "uint16"},
23: { "name":"sport","type": "sport"},
24: { "name":"event_group","type": "uint8"},
25: { "name":"nec_lat","type": "sint32"},
26: { "name":"nec_long","type": "sint32"},
27: { "name":"swc_lat","type": "sint32"},
28: { "name":"swc_long","type": "sint32"},
29: { "name":"name","type": "string"},
30: { "name":"normalized_power","type": "uint16"},
31: { "name":"left_right_balance","type": "left_right_balance_100"},
32: { "name":"sub_sport","type": "sub_sport"},
33: { "name":"total_work","type": "uint32"},
34: { "name":"avg_altitude","type": "uint16"},
35: { "name":"max_altitude","type": "uint16"},
36: { "name":"gps_accuracy","type": "uint8"},
37: { "name":"avg_grade","type": "sint16"},
38: { "name":"avg_pos_grade","type": "sint16"},
39: { "name":"avg_neg_grade","type": "sint16"},
40: { "name":"max_pos_grade","type": "sint16"},
41: { "name":"max_neg_grade","type": "sint16"},
42: { "name":"avg_temperature","type": "sint8"},
43: { "name":"max_temperature","type": "sint8"},
44: { "name":"total_moving_time","type": "uint32"},
45: { "name":"avg_pos_vertical_speed","type": "sint16"},
46: { "name":"avg_neg_vertical_speed","type": "sint16"},
47: { "name":"max_pos_vertical_speed","type": "sint16"},
48: { "name":"max_neg_vertical_speed","type": "sint16"},
49: { "name":"time_in_hr_zone","type": "uint32"},
50: { "name":"time_in_speed_zone","type": "uint32"},
51: { "name":"time_in_cadence_zone","type": "uint32"},
52: { "name":"time_in_power_zone","type": "uint32"},
53: { "name":"repetition_num","type": "uint16"},
54: { "name":"min_altitude","type": "uint16"},
55: { "name":"min_heart_rate","type": "uint8"},
56: { "name":"active_time","type": "uint32"},
57: { "name":"wkt_step_index","type": "message_index"},
58: { "name":"sport_event","type": "sport_event"},
59: { "name":"avg_left_torque_effectiveness","type": "uint8"},
60: { "name":"avg_right_torque_effectiveness","type": "uint8"},
61: { "name":"avg_left_pedal_smoothness","type": "uint8"},
62: { "name":"avg_right_pedal_smoothness","type": "uint8"},
63: { "name":"avg_combined_pedal_smoothness","type": "uint8"},
64: { "name":"status","type": "segment_lap_status"},
65: { "name":"uuid","type": "string"},
66: { "name":"avg_fractional_cadence","type": "uint8"},
67: { "name":"max_fractional_cadence","type": "uint8"},
68: { "name":"total_fractional_cycles","type": "uint8"},
69: { "name":"front_gear_shift_count","type": "uint16"},
70: { "name":"rear_gear_shift_count","type": "uint16"},
71: { "name":"time_standing","type": "uint32"},
72: { "name":"stand_count","type": "uint16"},
73: { "name":"avg_left_pco","type": "sint8"},
74: { "name":"avg_right_pco","type": "sint8"},
75: { "name":"avg_left_power_phase","type": "uint8"},
76: { "name":"avg_left_power_phase_peak","type": "uint8"},
77: { "name":"avg_right_power_phase","type": "uint8"},
78: { "name":"avg_right_power_phase_peak","type": "uint8"},
79: { "name":"avg_power_position","type": "uint16"},
80: { "name":"max_power_position","type": "uint16"},
81: { "name":"avg_cadence_position","type": "uint8"},
82: { "name":"max_cadence_position","type": "uint8"},
83: { "name":"manufacturer","type": "manufacturer"},
84: { "name":"total_grit","type": "float32"},
85: { "name":"total_flow","type": "float32"},
86: { "name":"avg_grit","type": "float32"},
87: { "name":"avg_flow","type": "float32"}
}

segment_file = {
254: { "name":"message_index","type": "message_index"},
1: { "name":"file_uuid","type": "string"},
3: { "name":"enabled","type": "bool"},
4: { "name":"user_profile_primary_key","type": "uint32"},
7: { "name":"leader_type","type": "segment_leaderboard_type"},
8: { "name":"leader_group_primary_key","type": "uint32"},
9: { "name":"leader_activity_id","type": "uint32"},
10: { "name":"leader_activity_id_string","type": "string"},
11: { "name":"default_race_leader","type": "uint8"}
}

workout = {
4: { "name":"sport","type": "sport"},
5: { "name":"capabilities","type": "workout_capabilities"},
6: { "name":"num_valid_steps","type": "uint16"},
8: { "name":"wkt_name","type": "string"},
11: { "name":"sub_sport","type": "sub_sport"},
14: { "name":"pool_length","type": "uint16"},
15: { "name":"pool_length_unit","type": "display_measure"}
}

workout_session = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"sport","type": "sport"},
1: { "name":"sub_sport","type": "sub_sport"},
2: { "name":"num_valid_steps","type": "uint16"},
3: { "name":"first_step_index","type": "uint16"},
4: { "name":"pool_length","type": "uint16"},
5: { "name":"pool_length_unit","type": "display_measure"}
}

workout_step = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"wkt_step_name","type": "string"},
1: { "name":"duration_type","type": "wkt_step_duration"},
2: { "name":"duration_value","type": "uint32"},
3: { "name":"target_type","type": "wkt_step_target"},
4: { "name":"target_value","type": "uint32"},
5: { "name":"custom_target_value_low","type": "uint32"},
6: { "name":"custom_target_value_high","type": "uint32"},
7: { "name":"intensity","type": "intensity"},
8: { "name":"notes","type": "string"},
9: { "name":"equipment","type": "workout_equipment"},
10: { "name":"exercise_category","type": "exercise_category"},
11: { "name":"exercise_name","type": "uint16"},
12: { "name":"exercise_weight","type": "uint16"},
13: { "name":"weight_display_unit","type": "fit_base_unit"}
}

exercise_title = {
254: { "name":"message_index","type": "message_index"},
0: { "name":"exercise_category","type": "exercise_category"},
1: { "name":"exercise_name","type": "uint16"},
2: { "name":"wkt_step_name","type": "string"}
}

schedule = {
0: { "name":"manufacturer","type": "manufacturer"},
1: { "name":"product","type": "uint16"},
2: { "name":"serial_number","type": "uint32z"},
3: { "name":"time_created","type": "date_time"},
4: { "name":"completed","type": "bool"},
5: { "name":"type","type": "schedule"},
6: { "name":"scheduled_time","type": "local_date_time"}
}

totals = {
254: { "name":"message_index","type": "message_index"},
253: { "name":"timestamp","type": "date_time"},
0: { "name":"timer_time","type": "uint32"},
1: { "name":"distance","type": "uint32"},
2: { "name":"calories","type": "uint32"},
3: { "name":"sport","type": "sport"},
4: { "name":"elapsed_time","type": "uint32"},
5: { "name":"sessions","type": "uint16"},
6: { "name":"active_time","type": "uint32"},
9: { "name":"sport_index","type": "uint8"}
}

weight_scale = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"weight","type": "weight"},
1: { "name":"percent_fat","type": "uint16"},
2: { "name":"percent_hydration","type": "uint16"},
3: { "name":"visceral_fat_mass","type": "uint16"},
4: { "name":"bone_mass","type": "uint16"},
5: { "name":"muscle_mass","type": "uint16"},
7: { "name":"basal_met","type": "uint16"},
8: { "name":"physique_rating","type": "uint8"},
9: { "name":"active_met","type": "uint16"},
10: { "name":"metabolic_age","type": "uint8"},
11: { "name":"visceral_fat_rating","type": "uint8"},
12: { "name":"user_profile_index","type": "message_index"}
}

blood_pressure = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"systolic_pressure","type": "uint16"},
1: { "name":"diastolic_pressure","type": "uint16"},
2: { "name":"mean_arterial_pressure","type": "uint16"},
3: { "name":"map_3_sample_mean","type": "uint16"},
4: { "name":"map_morning_values","type": "uint16"},
5: { "name":"map_evening_values","type": "uint16"},
6: { "name":"heart_rate","type": "uint8"},
7: { "name":"heart_rate_type","type": "hr_type"},
8: { "name":"status","type": "bp_status"},
9: { "name":"user_profile_index","type": "message_index"}
}

monitoring_info = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"local_timestamp","type": "local_date_time"},
1: { "name":"activity_type","type": "activity_type"},
3: { "name":"cycles_to_distance","type": "uint16"},
4: { "name":"cycles_to_calories","type": "uint16"},
5: { "name":"resting_metabolic_rate","type": "uint16"}
}

monitoring = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"device_index","type": "device_index"},
1: { "name":"calories","type": "uint16"},
2: { "name":"distance","type": "uint32"},
3: { "name":"cycles","type": "uint32"},
4: { "name":"active_time","type": "uint32"},
5: { "name":"activity_type","type": "activity_type"},
6: { "name":"activity_subtype","type": "activity_subtype"},
7: { "name":"activity_level","type": "activity_level"},
8: { "name":"distance_16","type": "uint16"},
9: { "name":"cycles_16","type": "uint16"},
10: { "name":"active_time_16","type": "uint16"},
11: { "name":"local_timestamp","type": "local_date_time"},
12: { "name":"temperature","type": "sint16"},
14: { "name":"temperature_min","type": "sint16"},
15: { "name":"temperature_max","type": "sint16"},
16: { "name":"activity_time","type": "uint16"},
19: { "name":"active_calories","type": "uint16"},
24: { "name":"current_activity_type_intensity","type": "byte"},
25: { "name":"timestamp_min_8","type": "uint8"},
26: { "name":"timestamp_16","type": "uint16"},
27: { "name":"heart_rate","type": "uint8"},
28: { "name":"intensity","type": "uint8"},
29: { "name":"duration_min","type": "uint16"},
30: { "name":"duration","type": "uint32"},
31: { "name":"ascent","type": "uint32"},
32: { "name":"descent","type": "uint32"},
33: { "name":"moderate_activity_minutes","type": "uint16"},
34: { "name":"vigorous_activity_minutes","type": "uint16"}
}

hr = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"fractional_timestamp","type": "uint16"},
1: { "name":"time256","type": "uint8"},
6: { "name":"filtered_bpm","type": "uint8"},
9: { "name":"event_timestamp","type": "uint32"},
10: { "name":"event_timestamp_12","type": "byte"}
}

stress_level = {
0: { "name":"stress_level_value","type": "sint16"},
1: { "name":"stress_level_time","type": "date_time"}
}

memo_glob = {
250: { "name":"part_index","type": "uint32"},
0: { "name":"memo","type": "byte"},
1: { "name":"message_number","type": "uint16"},
2: { "name":"message_index","type": "message_index"}
}

ant_channel_id = {
0: { "name":"channel_number","type": "uint8"},
1: { "name":"device_type","type": "uint8z"},
2: { "name":"device_number","type": "uint16z"},
3: { "name":"transmission_type","type": "uint8z"},
4: { "name":"device_index","type": "device_index"}
}

ant_rx = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"fractional_timestamp","type": "uint16"},
1: { "name":"mesg_id","type": "byte"},
2: { "name":"mesg_data","type": "byte"},
3: { "name":"channel_number","type": "uint8"},
4: { "name":"data","type": "byte"}
}

ant_tx = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"fractional_timestamp","type": "uint16"},
1: { "name":"mesg_id","type": "byte"},
2: { "name":"mesg_data","type": "byte"},
3: { "name":"channel_number","type": "uint8"},
4: { "name":"data","type": "byte"}
}

exd_screen_configuration = {
0: { "name":"screen_index","type": "uint8"},
1: { "name":"field_count","type": "uint8"},
2: { "name":"layout","type": "exd_layout"},
3: { "name":"screen_enabled","type": "bool"}
}

exd_data_field_configuration = {
0: { "name":"screen_index","type": "uint8"},
1: { "name":"concept_field","type": "byte"},
2: { "name":"field_id","type": "uint8"},
3: { "name":"concept_count","type": "uint8"},
4: { "name":"display_type","type": "exd_display_type"},
5: { "name":"title","type": "string"}
}

exd_data_concept_configuration = {
0: { "name":"screen_index","type": "uint8"},
1: { "name":"concept_field","type": "byte"},
2: { "name":"field_id","type": "uint8"},
3: { "name":"concept_index","type": "uint8"},
4: { "name":"data_page","type": "uint8"},
5: { "name":"concept_key","type": "uint8"},
6: { "name":"scaling","type": "uint8"},
8: { "name":"data_units","type": "exd_data_units"},
9: { "name":"qualifier","type": "exd_qualifiers"},
10: { "name":"descriptor","type": "exd_descriptors"},
11: { "name":"is_signed","type": "bool"}
}

field_description = {
0: { "name":"developer_data_index","type": "uint8"},
1: { "name":"field_definition_number","type": "uint8"},
2: { "name":"fit_base_type_id","type": "fit_base_type"},
3: { "name":"field_name","type": "string"},
4: { "name":"array","type": "uint8"},
5: { "name":"components","type": "string"},
6: { "name":"scale","type": "uint8"},
7: { "name":"offset","type": "sint8"},
8: { "name":"units","type": "string"},
9: { "name":"bits","type": "string"},
10: { "name":"accumulate","type": "string"},
13: { "name":"fit_base_unit_id","type": "fit_base_unit"},
14: { "name":"native_mesg_num","type": "mesg_num"},
15: { "name":"native_field_num","type": "uint8"}
}

developer_data_id = {
0: { "name":"developer_id","type": "byte"},
1: { "name":"application_id","type": "byte"},
2: { "name":"manufacturer_id","type": "manufacturer"},
3: { "name":"developer_data_index","type": "uint8"},
4: { "name":"application_version","type": "uint32"}
}

dive_summary = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"reference_mesg","type": "mesg_num"},
1: { "name":"reference_index","type": "message_index"},
2: { "name":"avg_depth","type": "uint32"},
3: { "name":"max_depth","type": "uint32"},
4: { "name":"surface_interval","type": "uint32"},
5: { "name":"start_cns","type": "uint8"},
6: { "name":"end_cns","type": "uint8"},
7: { "name":"start_n2","type": "uint16"},
8: { "name":"end_n2","type": "uint16"},
9: { "name":"o2_toxicity","type": "uint16"},
10: { "name":"dive_number","type": "uint32"},
11: { "name":"bottom_time","type": "uint32"}
}

climb_pro = {
253: { "name":"timestamp","type": "date_time"},
0: { "name":"position_lat","type": "sint32"},
1: { "name":"position_long","type": "sint32"},
2: { "name":"climb_pro_event","type": "climb_pro_event"},
3: { "name":"climb_number","type": "uint16"},
4: { "name":"climb_category","type": "uint8"},
5: { "name":"current_dist","type": "float32"}
}

fit_messages = {
"file_id":file_id,
"file_creator":file_creator,
"timestamp_correlation":timestamp_correlation,
"software":software,
"slave_device":slave_device,
"capabilities":capabilities,
"file_capabilities":file_capabilities,
"mesg_capabilities":mesg_capabilities,
"field_capabilities":field_capabilities,
"device_settings":device_settings,
"user_profile":user_profile,
"hrm_profile":hrm_profile,
"sdm_profile":sdm_profile,
"bike_profile":bike_profile,
"connectivity":connectivity,
"watchface_settings":watchface_settings,
"ohr_settings":ohr_settings,
"zones_target":zones_target,
"sport":sport,
"hr_zone":hr_zone,
"speed_zone":speed_zone,
"cadence_zone":cadence_zone,
"power_zone":power_zone,
"met_zone":met_zone,
"dive_settings":dive_settings,
"dive_alarm":dive_alarm,
"dive_gas":dive_gas,
"goal":goal,
"activity":activity,
"session":session,
"lap":lap,
"length":length,
"record":record,
"event":event,
"device_info":device_info,
"training_file":training_file,
"hrv":hrv,
"weather_conditions":weather_conditions,
"weather_alert":weather_alert,
"gps_metadata":gps_metadata,
"camera_event":camera_event,
"gyroscope_data":gyroscope_data,
"accelerometer_data":accelerometer_data,
"magnetometer_data":magnetometer_data,
"barometer_data":barometer_data,
"three_d_sensor_calibration":three_d_sensor_calibration,
"one_d_sensor_calibration":one_d_sensor_calibration,
"video_frame":video_frame,
"obdii_data":obdii_data,
"nmea_sentence":nmea_sentence,
"aviation_attitude":aviation_attitude,
"video":video,
"video_title":video_title,
"video_description":video_description,
"video_clip":video_clip,
"set":fit_set,
"jump":jump,
"course":course,
"course_point":course_point,
"segment_id":segment_id,
"segment_leaderboard_entry":segment_leaderboard_entry,
"segment_point":segment_point,
"segment_lap":segment_lap,
"segment_file":segment_file,
"workout":workout,
"workout_session":workout_session,
"workout_step":workout_step,
"exercise_title":exercise_title,
"schedule":schedule,
"totals":totals,
"weight_scale":weight_scale,
"blood_pressure":blood_pressure,
"monitoring_info":monitoring_info,
"monitoring":monitoring,
"hr":hr,
"stress_level":stress_level,
"memo_glob":memo_glob,
"ant_channel_id":ant_channel_id,
"ant_rx":ant_rx,
"ant_tx":ant_tx,
"exd_screen_configuration":exd_screen_configuration,
"exd_data_field_configuration":exd_data_field_configuration,
"exd_data_concept_configuration":exd_data_concept_configuration,
"field_description":field_description,
"developer_data_id":developer_data_id,
"dive_summary":dive_summary,
"climb_pro":climb_pro
}

# function to convert from a Global Message Number, to get the definition Name
def getMessage(globalMessageNumName,fieldDefnNumber):
    messageDict = fit_messages[globalMessageNumName]
    return messageDict[fieldDefnNumber]["name"]

def getMessageType(globalMessageNumName,fieldDefnNumber):
    messageDict = fit_messages[globalMessageNumName]
    return messageDict[fieldDefnNumber]["type"]
