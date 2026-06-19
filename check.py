from src.training.config.settings import Settings

settings = Settings()

log_path = settings.log_path
diabetes_dataset_path = settings.diabetes_dataset_path
heart_disease_dataset_path = settings.heart_disease_dataset_path
diabetes_model_path = settings.diabetes_model_path
heart_disease_model_path = settings.heart_disease_model_path
diabetes_target_col = settings.diabetes_target_col
heart_disease_target_col = settings.heart_disease_target_col
test_size = settings.test_size
random_state = settings.random_state
hyper_params_yaml_path = settings.hyper_params_yaml_path

print("All settings loaded successfully:")
print(f"Log Path: {log_path}")
print(f"Diabetes Dataset Path: {diabetes_dataset_path}")
print(f"Heart Disease Dataset Path: {heart_disease_dataset_path}")
print(f"Diabetes Model Path: {diabetes_model_path}")
print(f"Heart Disease Model Path: {heart_disease_model_path}")
print(f"Diabetes Target Column: {diabetes_target_col}")
print(f"Heart Disease Target Column: {heart_disease_target_col}")
print(f"Test Size: {test_size}")
print(f"Random State: {random_state}")
print(f"Hyperparameters YAML Path: {hyper_params_yaml_path}")