# %%
from pipeline.generate_prompt_rollouts import generate_rollouts
from pipeline.store_activations import store_activations
from pipeline.load_activations import prepare_dataloaders
from pipeline.train_probe import train_probe

# %%
if __name__ == "__main__":
    '''generate_rollouts(
        model_name="Qwen/Qwen3-4B",
        prompts_path="/workspace/llm-progress-monitor/splits/harmless_train.json",
        num_rollouts=1000,
        max_tokens=32768,
        save_path="/workspace/llm-progress-monitor/rollouts-test",
        thinking_mode=2, # 0: no thinking, 1: thinking, 2: both (for 100 rollouts, use 50 prompts x 2)
    )'''

    store_activations(
        model_name="Qwen/Qwen3-4B",
        rollouts_path="rollouts-big/Qwen3-4B-2.json",
        activations_dir="/workspace/llm-progress-monitor/rollouts-big/activations",
        layer_idx=15
    )

    '''train_dataloader, test_dataloader, stats = prepare_dataloaders(
        activations_dir="/workspace/llm-progress-monitor/rollouts-big/activations",
        batch_size=1024,
        test_size=0.2
    )'''
    
    '''print(f"Dataset stats: {stats}")
    print(f"Train dataloader: {len(train_dataloader)} batches")
    print(f"Test dataloader: {len(test_dataloader)} batches")'''
    
    # Stage 4: Train probe
    '''model, training_stats = train_probe(
        activations_dir="/workspace/llm-progress-monitor/rollouts-big/activations",
        batch_size=1024,
        n_epochs=1,
        learning_rate=0.0001,
        save_path="/workspace/llm-progress-monitor/rollouts-big/probe_weights.pt"
    )
    
    print(f"Training completed!")
    print(f"Final train loss: {training_stats.final_train_loss:.4f}")
    print(f"Final test loss: {training_stats.final_test_loss:.4f}")
    print(f"Model saved to: /workspace/llm-progress-monitor/rollouts-big/probe_weights.pt")'''