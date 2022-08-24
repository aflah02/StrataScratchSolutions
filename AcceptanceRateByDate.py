import numpy
import pandas
sent = fb_friend_requests[fb_friend_requests['action']=='sent']
accepted = fb_friend_requests[fb_friend_requests['action']=='accepted']
joined_table = sent.merge(accepted, left_on=['user_id_sender', 'user_id_receiver'], right_on=['user_id_sender', 'user_id_receiver'], how='left')
joined_table_with_accepted_only = joined_table.dropna()
joined_table_with_accepted_only['counts_accepted'] = joined_table_with_accepted_only.groupby(['date_x'])['date_x'].transform('count')
joined_table['counts_sent'] = joined_table.groupby(['date_x'])['date_x'].transform('count')
joined_table = joined_table.drop_duplicates(subset=['date_x'])[['date_x', 'counts_sent']]
joined_table_with_accepted_only = joined_table_with_accepted_only.drop_duplicates(subset=['date_x'])[['date_x', 'counts_accepted']]
joined_table = joined_table.merge(joined_table_with_accepted_only, left_on=['date_x'], right_on=['date_x'], how='left')
joined_table['acceptance_rate'] = joined_table['counts_accepted']/joined_table['counts_sent']
joined_table = joined_table[['date_x', 'acceptance_rate']]
joined_table
