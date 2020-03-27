import ray
import ray.tune as tune

if __name__ == "__main__":
   ray.init(redis_address = 'localhost:6379')

   tune.run("PPO",   
            config={
               "env": "CartPole-v0",
               "num_gpus": 0,
               "num_workers": 1
            },
            stop={
               "episode_reward_mean": 200,
               "time_total_s": 600
            },
            checkpoint_at_end=True,
            local_dir='./logs'
            )
