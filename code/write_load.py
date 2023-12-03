import ast

def load_env(env_file_path):

    '''
    ---
    Load the environment configuration file

    env_file_path -- path to the configuration file 
    ---
    '''

    with open(env_file_path, 'r') as f:
        env_config = {}
        for line in f:
            k, v = line.strip().split('=')
            env_config[k.strip()] = ast.literal_eval(v.strip())
    
    return env_config 