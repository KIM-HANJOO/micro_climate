#   < new directory paths >
samples_module_dir = Path(os.getcwd())
sample_robby = samples_module_dir.parent
sample_data = os.path.join(sample_robby, 'preprocessed', 'merged')
sample_info = os.path.join(sample_robby, 'preprocessed', 'info')
sample_plot = os.path.join(sample_robby, 'preprocessed', 'plot')
sample_typo = os.path.join(sample_robby, 'preprocessed', 'typo')
sample_time = os.path.join(sample_robby, 'preprocessed', 'time')
sample_only_time = os.path.join(sample_robby, 'preprocessed', 'only_available_time')
sample_avail = sample_only_time
sample_round = os.path.join(sample_robby, 'preprocessed', 'rounded')
sample_rounded = sample_rounded


main_dir = sample_robby#.parent
module_dir = os.path.join(main_dir, 'module')

datas_dir = os.path.join(main_dir, 'datas')
self_module = os.path.join(module_dir, 'self_module')
info_dir = os.path.join(main_dir, 'info_data')


#   add dirs to sys.path

sys.path.append(module_dir)
sys.path.append(self_module)

#   import self packages

import directory_change as dich
import discordlib_pyplot as dlt


dich.newfolder(sample_data)
dich.newfolder(sample_info)
dich.newfolder(sample_plot)
dich.newfolder(sample_typo)
dich.newfolder(sample_time)
dich.newfolder(sample_only_time)
