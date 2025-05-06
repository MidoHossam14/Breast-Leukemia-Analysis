import os
import arff
import pandas as pd

def convert_arff_file(arff_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(arff_path, 'r') as f:
        data = arff.load(f)
        df = pd.DataFrame(data['data'], columns=[attr[0] for attr in data['attributes']])
        
        base_name = os.path.basename(arff_path).replace(".arff", ".csv")
        output_path = os.path.join(output_dir, base_name)
        df.to_csv(output_path, index=False)
        
if __name__ == "__main__" :
    arff_path = [r"EKNN_Ensemble_KNN_Based_Classifier\EKNN\data\arff\Breast.arff",r"EKNN_Ensemble_KNN_Based_Classifier\EKNN\data\arff\Leukemia.arff"]
    output_dir = r"Breast-Leukemia-Analysis\data"
    for path in arff_path:
        convert_arff_file(path, output_dir)
    print("Conversion completed.")
    
    
    