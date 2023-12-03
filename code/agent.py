import numpy as np
from environment import Environment

class DynaAgent(Environment):

    def __init__(self, alpha, gamma):

        '''
        Initialise the agent class instance

        Input arguments:
            alpha -- learning rate \in (0, 1)
            gamma -- discount factor \in (0, 1)
        '''

        self.alpha = alpha
        self.gamma = gamma 

        return None

    def init_env(self, **env_config):

        Environment.__init__(**env_config)
        self._init_q_values()
        self._init_experience_buffer()

        return None
    
    def _init_q_values(self):

        '''
        Initialise Q-value table
        '''

        self.Q = np.zeros((self.num_states, self.num_actions))

        return None
    
    def _init_experience_buffer(self):
        
        '''
        Initialise the experience buffer
        '''

        self.experience_buffer = np.empty((0, 4))

        return None
    
    def _update_experience_buffer(self, s, a, r, s1):

        '''
        Complete the update function

        Input arguments:
            s  -- initial state
            a  -- chosen action
            r  -- received reward
            s1 -- next state
        '''

        return None
    
    def _update_q_values(self, s, a, r, s1):

        '''
        Complete the update function.

        Input arguments:
            s  -- initial state
            a  -- chosen action
            r  -- received reward
            s1 -- next state
        '''

        return None
    
    def _policy(self, s):

        '''
        Complete the policy function. 

        Input arguments:
            s -- state

        Output:
            a -- index action to be chosen
        '''
    
        return None
    
    def _plan(self, num_planning_updates):

        '''
        Complete the planning function

        Input arguments:
            num_planning_updates -- number of planning updates to execute
        '''

        return None
    
    def simulate(self, num_trials, num_planning_updates=None):

        '''
        Main simulation function

        Input arguments:
            num_trials -- number of trials (i.e., moves) to simulate
        '''

        self.history = np.empty((0, 4), dtype=int)
        s = self.start_state

        for _ in range(num_trials):
            
            # choose action
            a  = self._policy(s)
            # get new state
            s1 = np.random.choice(np.arange(self.num_states, p=self.T[s, a, :]))
            # receive reward
            r  = self.R[s, a]
            # learning
            self._update_q_values(s, a, r, s1)

            # update history
            self.history = np.vstack((self.history, np.array([s, a, r, s1])))

            if s1 == self.goal_state:
                if num_planning_updates is not None:
                    self._plan(num_planning_updates)
                s = self.start_state
            else:
                s = s1

        return None