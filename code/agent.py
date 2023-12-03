import numpy as np
from environment import Environment

class DynaAgent(Environment):

    def __init__(self, beta, gamma, epsilon):

        '''
        Initialise the agent class instance

        Input arguments:
            beta    -- learning rate \in (0, 1)
            gamma   -- discount factor \in (0, 1)
            epsilon -- controls the influence of the exploration bonus
        '''

        self.beta    = beta
        self.gamma   = gamma 
        self.epsilon = epsilon

        return None

    def init_env(self, **env_config):

        Environment.__init__(self, **env_config)

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
    
    def _init_history(self):

        self.history = np.empty((0, 4), dtype=int)

        return None
    
    def _init_action_count(self):

        self.action_count = np.zeros((self.num_states, self.num_actions))

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
    
    def _update_qvals(self, s, a, r, s1):

        '''
        Complete the update function.

        Input arguments:
            s  -- initial state
            a  -- chosen action
            r  -- received reward
            s1 -- next state
        '''

        return None
    
    def _update_action_count(self, s, a, r, s1):

        '''
        Complete the update funciton

        Input arguments:
            Input arguments:
            s  -- initial state
            a  -- chosen action
            r  -- received reward
            s1 -- next state
        '''

        return None
    
    def _update_history(self, s, a, r, s1):

        self.history = np.vstack((self.history, np.array([self.s, a, r, s1])))

        return None
    
    def _policy(self, s):

        '''
        Complete the policy function. 

        Input arguments:
            s -- state

        Output:
            a -- index of action to be chosen
        '''
    
        return None
    
    def _plan(self, num_planning_updates):

        '''
        Complete the planning function

        Input arguments:
            num_planning_updates -- number of planning updates to execute
        '''

        return None
    
    def get_performace(self):

        return np.cumsum(self.history[:, 2])
    
    def simulate(self, num_trials, reset_agent=True, num_planning_updates=None):

        '''
        Main simulation function

        Input arguments:
            num_trials -- number of trials (i.e., moves) to simulate
        '''

        if reset_agent:
            self._init_q_values()
            self._init_experience_buffer()
            self._init_action_count()
            self._init_history()
            
            self.s = self.start_state

        for _ in range(num_trials):
            
            # choose action
            a  = self._policy(self.s)
            # get new state
            s1 = np.random.choice(np.arange(self.num_states, p=self.T[self.s, a, :]))
            # receive reward
            r  = self.R[self.s, a]
            # learning
            self._update_qvals(self.s, a, r, s1)
            # update world model 
            self._update_experience_buffer(self.s, a, r, s1)
            # reset action count
            self._update_action_count(self.s, a, r, s1)
            # plan
            if num_planning_updates is not None:
                self._plan(num_planning_updates)

            # update history
            self._update_history(self.s, a, r, s1)

            if s1 == self.goal_state:
                self.s = self.start_state
            else:
                self.s = s1

        return None