from pipelines.train_pipeline import training_pipeline

if __name__ == "__main__":
    path = 'data/olist_customers_dataset.csv'
    training_pipeline(path)