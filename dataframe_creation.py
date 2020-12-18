import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns',500)
# used for sorting
from operator import itemgetter

def get_pbp_columns():
    # these are the columns of the data frame
    # these are year-spanning stats
    columns = ['Date',
               'game_in_series',
               'day_of_week',
               'away_team',
               'away_league',
               'away_team_game_number',
               'home_team',
               'home_league',
               'home_team_game_number',
               'away_team_score',
               'home_team_score',
               'number_of_outs',
               'day_or_night',
               'date_game_completed',
               'forfeit_info',
               'protest_info',
               'park_id',
               'attendance',
               'time_of_game',
               'away_line_scores',
               'home_line_scores',
               'away_at_bats',
               'away_hits',
               'away_doubles',
               'away_triples',
               'away_hrs',
               'away_rbi',
               'away_sh',
               'away_sf',
               'away_hbp',
               'away_walk',
               'away_int_walk',
               'away_so',
               'away_sb',
               'away_cs',
               'away_gidp',
               'away_catch_interference',
               'away_left_on_base',
               'away_pitchers_used',
               'away_pitch_earned_runs',
               'away_team_earned_runs',
               'away_pitch_wild_pitches',
               'away_pitch_balks',
               'away_def_putouts',
               'away_def_assists',
               'away_def_errors',
               'away_def_passed_balls',
               'away_def_double_plays',
               'away_def_triple_plays',
               'home_at_bats',
               'home_hits',
               'home_doubles',
               'home_triples',
               'home_hrs',
               'home_rbi',
               'home_sh',
               'home_sf',
               'home_hbp',
               'home_walk',
               'home_int_walk',
               'home_so',
               'home_sb',
               'home_cs',
               'home_gidp',
               'home_catch_interference',
               'home_left_on_base',
               'home_pitchers_used',
               'home_pitch_earned_runs',
               'home_team_earned_runs',
               'home_pitch_wild_pitches',
               'home_pitch_balks',
               'home_def_putouts',
               'home_def_assists',
               'home_def_errors',
               'home_def_passed_balls',
               'home_def_double_plays',
               'home_def_triple_plays',
               'hb_ump_id',
               'hb_ump_name',
               '1b_ump_id',
               '1b_ump_name',
               '2b_ump_id',
               '2b_ump_name',
               '3b_ump_id',
               '3b_ump_name',
               'lf_ump_id',
               'lf_ump_name',
               'rf_ump_id',
               'rf_ump_name',
               'away_team_manager_id',
               'away_team_manager_name',
               'home_team_manager_id',
               'home_team_manager_name',
               'win_pitch_id',
               'win_pitch_name',
               'lose_pitch_id',
               'lose_pitch_name',
               'save_pitch_id',
               'save_pitch_name',
               'game_win_rbi_batter_id',
               'game_win_rbi_batter_name',
               'away_start_pitch_id',
               'away_start_pitch_name',
               'home_start_pitch_id',
               'home_start_pitch_name',
               'away_player_1_id',
               'away_player_1_name',
               'away_player_1_def_pos',
               'away_player_2_id',
               'away_player_2_name',
               'away_player_2_def_pos',
               'away_player_3_id',
               'away_player_3_name',
               'away_player_3_def_pos',
               'away_player_4_id',
               'away_player_4_name',
               'away_player_4_def_pos',
               'away_player_5_id',
               'away_player_5_name',
               'away_player_5_def_pos',
               'away_player_6_id',
               'away_player_6_name',
               'away_player_6_def_pos',
               'away_player_7_id',
               'away_player_7_name',
               'away_player_7_def_pos',
               'away_player_8_id',
               'away_player_8_name',
               'away_player_8_def_pos',
               'away_player_9_id',
               'away_player_9_name',
               'away_player_9_def_pos',
               'home_player_1_id',
               'home_player_1_name',
               'home_player_1_def_pos',
               'home_player_2_id',
               'home_player_2_name',
               'home_player_2_def_pos',
               'home_player_3_id',
               'home_player_3_name',
               'home_player_3_def_pos',
               'home_player_4_id',
               'home_player_4_name',
               'home_player_4_def_pos',
               'home_player_5_id',
               'home_player_5_name',
               'home_player_5_def_pos',
               'home_player_6_id',
               'home_player_6_name',
               'home_player_6_def_pos',
               'home_player_7_id',
               'home_player_7_name',
               'home_player_7_def_pos',
               'home_player_8_id',
               'home_player_8_name',
               'home_player_8_def_pos',
               'home_player_9_id',
               'home_player_9_name',
               'home_player_9_def_pos',
               'additional_info',
               'acquisition_info',]
    return columns

def create_game_number(df):
    year_list = list(range(2000,2020,1))
    test_dict = {}
    team_list = df.home_team.unique()
    for year in year_list:
        test_dict[year] = {}
        for team in team_list:
            test_dict[year][team] = []
    # inserting games into the correct container
    # sorted by year the team
    for index,row in df.iterrows():
        test_dict[row.year][row.home_team].append(row.id)
    df.game_number_of_season = ''
    for year in test_dict:
        for team in test_dict[year]:
            counter=1
            for game in test_dict[year][team]:
                df[(df.id == game)].game_number_of_season = counter
                counter+=1
    return df.game_number_of_season

def create_win_next_game(df):
    year_list = range(2000,2020)
    team_list = df.home_team.unique()
    # this is going to be the target for the non-cumulative data set
    # did they win their next game
    # creating the blank dictionary split by year then team
    next_game_win_dict = {}
    for year in year_list:
        next_game_win_dict[year] = {}
        for team in team_list:
            next_game_win_dict[year][team] = []
    
    # appending every game id and outcome to each team for their year
    # this will append the outcome of this game 
    # you have the game id, then the outcome of that game
    for year in year_list:
        for team in team_list:
            for game in df[(df.Date.dt.year == year)&((df.home_team == team)|(df.away_team == team))][['id','home_outcome']].values.tolist():
                next_game_win_dict[year][team].append([game[0],game[1]])
    # appending the outcome of the next game (doing this in reverse)
    # so game 81 is seen first and assigns the outcome of this game to game 80
    for year in year_list:
        for team in team_list:
            place_holder_outcome = -1
            place_holder_team = ''
            # starting from last game going to first
            for game in next_game_win_dict[year][team][::-1]:
                #print(team,game,place_holder_outcome)
                # 
                if team in place_holder_team:
                    game.append(place_holder_outcome)
                else:
                    if place_holder_outcome == 1:
                        game.append(0)
                    else:
                        game.append(1)
                # making this games outcome the next games outcome for the previous game
                place_holder_outcome = game[1]
                place_holder_team = game[0][0:3]

    df['target'] = ''
    # this creates the column
    for year in year_list:
        for team in team_list:
            for game in next_game_win_dict[year][team]:
                if team in game[0]:# only want home games
                    df.target[(df.id == game[0])] = game[2]
    return df.target
    
    
    
def create_home_won_prev(df):
    year_list = range(2000,2020)
    team_list = df.home_team.unique()
    # this is to determine if the home team won their last game
    home_won_last_game_column = []
    home_won_last_game_dict = {}
    # setting the teams outcomes to 0 for the first game as their was no previous game
    for team in team_list:
        home_won_last_game_dict[team] = 0
    for index,row in df.iterrows():
        # input num into row if they won last game
        # home team that is going to be column
        home_won_last_game_column.append(home_won_last_game_dict[row.home_team])
        home_team_outcome = row.home_outcome
        # seeing if they won their last game
        if home_team_outcome == 1:
            away_team_outcome = 0
        elif home_team_outcome == -1:
            away_team_outcome = -1
        else:
            away_team_outcome = 1
        # change home team
        home_won_last_game_dict[row.home_team] = home_team_outcome
        # change away team
        home_won_last_game_dict[row.away_team] = away_team_outcome
    return home_won_last_game_column

def create_away_won_prev(df):
    year_list = range(2000,2020)
    team_list = df.home_team.unique()
    # this is to determine if the away team won their last game
    away_won_last_game_column = []
    away_won_last_game_dict = {}
    # same process for first game
    for team in team_list:
        away_won_last_game_dict[team] = 0
    for index,row in df.iterrows():
        # input num into row if they won last game
        # home team that is going to be column
        away_won_last_game_column.append(away_won_last_game_dict[row.away_team])
        home_team_outcome = row.away_outcome
        if home_team_outcome == 1:
            away_team_outcome = 0
        elif home_team_outcome == -1:
            away_team_outcome = -1
        else:
            away_team_outcome = 1
        # change home team
        away_won_last_game_dict[row.away_team] = away_team_outcome
        # change away team
        away_won_last_game_dict[row.home_team] = home_team_outcome
    return away_won_last_game_column


def create_aggregate_data(df):
    df['Date'] = pd.to_datetime(df["Date"])
    # all team and years
    team_list = df.home_team.unique()
    year_list = df.Date.dt.year.unique()
    # dropping unnused columns
    cols_to_drop = ['forfeit_info', 'lf_ump_id', 'rf_ump_id', 'protest_info','date_game_completed','additional_info','save_pitch_id','game_win_rbi_batter_id','game_in_series','away_catch_interference','home_catch_interference','away_pitch_balks','home_pitch_balks','day_of_week','away_league','away_team_game_number','home_league','home_team_game_number','day_or_night','park_id','attendance','time_of_game','away_line_scores','home_line_scores','year','id','number_of_outs','target','away_won_last_game','home_won_last_game','game_number_of_season']
    df.drop(columns=cols_to_drop,inplace=True)
    df.drop(df.loc[:,'hb_ump_id':'acquisition_info'],axis=1,inplace=True)
    
    # making dummy rows for use in putting games into year/team buckets
    df['home_date'] = df.Date
    df['away_date'] = df.Date
    
    # initialize dict so that we can aggregate the stats of each team per year
    # final dict is where we are going to be adding the aggregated stats
    stat_dict = {}
    final_dict = {}
    for year in year_list:
        stat_dict[year] = {}
        final_dict[year] = {}
        for team in team_list:
            stat_dict[year][team] = []
            final_dict[year][team] = []
            
    # this is putting games into the correct year/team combo
    # we need both home and away games bc away games affect stats of the team
    # this will end in lists that contain every game for every team for every year
    # dict[year][team] = 161 lists of each games stats
    for year in year_list:
        for team in team_list:
            # home game stats
            for game in df[(df.Date.dt.year == year)&(df.home_team == team)].filter(regex='home').values.tolist():
                stat_dict[year][team].append(np.array(game))
            # away game stats
            for game in df[(df.Date.dt.year == year)&(df.away_team == team)].filter(regex='away').values.tolist():
                stat_dict[year][team].append(np.array(game))
                
    # have to sort each year/team array so that they are in the correct date order
    for year in year_list:
        for team in team_list:
            stat_dict[year][team] = sorted(stat_dict[year][team],key=itemgetter(-1))
            
    # putting date in the front to make it easier to work with
    for year in year_list:
        for team in team_list:
            year_team_stats = []
            for game in stat_dict[year][team]:
                year_team_stats.append(np.insert(game[:-1],0,game[-1]))
            stat_dict[year][team] = year_team_stats
    # this is aggregating the stats per year
    # so each game is the mean of all stats of that game and all previous
    # I am going to need to 
    for year in year_list:
        for team in team_list:
            curr_game_number = 1
            aggregate_stats = np.array(stat_dict[year][team][0][2:])
            for game in stat_dict[year][team]:
                header_info = game[0:2]
                contents = game[2:]
                aggregate_stats_current_game = aggregate_stats/curr_game_number
                aggregate_stats = contents+aggregate_stats
                final_dict[year][team].append(np.concatenate((header_info,aggregate_stats_current_game)))
                curr_game_number +=1
    
    agg_df = pd.DataFrame()
    # creating the aggregate stats array
    agg_array = []
    for year in year_list:
        for team in team_list:
            for game in final_dict[year][team]:
                agg_array.append(game)
    
    # making the array of all stats
    agg_df = pd.DataFrame(agg_array)
    # gets rid of team name and date
    away_data_column_names = list(df.filter(regex='away').columns)[1:-1] 
    # gets rid of team name and date
    home_data_column_names = list(df.filter(regex='home').columns)[1:-1]
    
    game_basic_info_df = df.iloc[:,0:3]
    for stat in away_data_column_names:
        game_basic_info_df[stat] = ''
    for stat in home_data_column_names:
        game_basic_info_df[stat] = ''
        
    final_matrix_for_df = []
    
    for index,row in game_basic_info_df.iterrows():
        # append home team aggregate stats
        home_data = agg_df[(agg_df[0] == row.Date)&(agg_df[1]==row.home_team)].iloc[:,2:].to_numpy()
        # append away team aggregate stats
        away_data = agg_df[(agg_df[0] == row.Date)&(agg_df[1]==row.away_team)].iloc[:,2:].to_numpy()
        # create the full row
        full_row = np.concatenate((home_data[0],away_data[0]))
        temp_array = [row.Date,row.home_team,row.away_team]
        for individual_stat in full_row:
            temp_array.append(individual_stat)
        final_matrix_for_df.append(temp_array)
    
    final_final_df = pd.DataFrame(final_matrix_for_df)
    
    columns_for_output_df = ['Date','home_team','away_team']
    
    
    for col_name in home_data_column_names:
        columns_for_output_df.append(col_name)
    for col_name in away_data_column_names:
        columns_for_output_df.append(col_name)
        
    final_final_df.columns = columns_for_output_df
    
    return final_final_df