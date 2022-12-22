import json
import os
import numpy as np
import pandas as pd
import pickle



def save_data(data : any, path : str, name : str, error : bool, format : str) -> int:

    """
    Save data to file
    :param data: data to save
    :param path: path to save
    :param name: name of file
    :param format: format of file
    :return: None
    """

    # check if the types of the variables are the good ones:
    if not isinstance(data, (dict, list, np.ndarray, pd.DataFrame)):
        if error:
            raise TypeError("data must be a dict, list, numpy array or pandas DataFrame")
        else:
            return 3

    if not isinstance(path, str):        
        if error:
            raise TypeError("path must be a string")
        else:
            return 2
    
    if not isinstance(name, str):
        if error:
            raise TypeError("name must be a string")
        else:
            return 1

    if not isinstance(format, str):
        if error:
            raise TypeError("format must be a string")
        else:
            return 4

    # Check if path exist and if not create it
    if not os.path.exists(path):
        os.makedirs(path)

    # Check if the name ends with .json
    if not name.endswith('.' + format):
        name = name + '.' + format

    # Save data to json file
    if format == 'json':
        with open(path + name, 'w') as outfile:
            json.dump(data, outfile, indent=4)

    # Save data to csv file
    elif format == 'csv':
        if isinstance(data, pd.DataFrame):
            data.to_csv(path + name, index=False)
        else:
            pd.DataFrame(data).to_csv(path + name, index=False)

    # Save data to txt file
    elif format == 'txt':
        if isinstance(data, pd.DataFrame):
            data.to_csv(path + name, index=False)
        else:
            pd.DataFrame(data).to_csv(path + name, index=False)

    else:
        if error:
            raise ValueError("format must be 'json', 'csv' or 'txt'")
        else:
            return 5

    return 0



def save_data_to_json(data : dict[any:any], path : str, name : str, error : bool) -> int :
    """
    Save data to json file
    :param data: data to save
    :param path: path to save
    :param name: name of file
    :return: None
    """

    # check if the types of the variables are the good ones:
    if not isinstance(data, dict):
        if error:
            raise TypeError("data must be a dict")
        else:
            return 3

    if not isinstance(path, str):        
        if error:
            raise TypeError("path must be a string")
        else:
            return 2
    
    if not isinstance(name, str):
        if error:
            raise TypeError("name must be a string")
        else:
            return 1

    # Check if path exist and if not create it
    if not os.path.exists(path):
        os.makedirs(path)
    
    # Check if the name ends with .json
    if not name.endswith('.json'):
        name = name + '.json'

    # Save data to json file
    with open(path + name, 'w') as outfile:
        json.dump(data, outfile, indent=4)

    return 0



def save_data_to_csv(data : any , path : str, name : str, error : bool) -> int:

    """
    Save data to csv file
    :param data: data to save
    :param path: path to save
    :param name: name of file
    :return: None
    """

    # check if the types of the variables are the good ones:
    if not isinstance(data, (dict, list, np.ndarray, pd.DataFrame)):
        if error:
            raise TypeError("data must be a dict, list, numpy array or pandas DataFrame")
        else:
            return 3

    if not isinstance(path, str):        
        if error:
            raise TypeError("path must be a string")
        else:
            return 2
    
    if not isinstance(name, str):
        if error:
            raise TypeError("name must be a string")
        else:
            return 1

    # Check if path exist and if not create it
    if not os.path.exists(path):
        os.makedirs(path)

    # Check if the name ends with .csv
    if not name.endswith('.csv'):
        name = name + '.csv'

    # Save data to csv file
    if isinstance(data, pd.DataFrame):
        data.to_csv(path + name, index=False)
    else:
        pd.DataFrame(data).to_csv(path + name, index=False)

    return 0



def save_data_to_txt(data : any , path : str, name : str, error : bool) -> int:

    """
    Save data to txt file
    :param data: data to save
    :param path: path to save
    :param name: name of file
    :return: None
    """

    # check if the types of the variables are the good ones:
    if not isinstance(data, (dict, list, np.ndarray, pd.DataFrame)):
        if error:
            raise TypeError("data must be a dict, list, numpy array or pandas DataFrame")
        else:
            return 3

    if not isinstance(path, str):        
        if error:
            raise TypeError("path must be a string")
        else:
            return 2
    
    if not isinstance(name, str):
        if error:
            raise TypeError("name must be a string")
        else:
            return 1

    # Check if path exist and if not create it
    if not os.path.exists(path):
        os.makedirs(path)

    # Check if the name ends with .txt 
    if not name.endswith('.txt'):
        name = name + '.txt'
    
    # Save data to txt file
    if isinstance(data, pd.DataFrame):
        data.to_csv(path + name, index=False)

    elif isinstance(data, np.ndarray):
        np.savetxt(path + name, data, delimiter=",")

    else:
        with open(path + name, 'w') as outfile:
            outfile.write(str(data))

    return 0



def save_data_to_pickle(data : any , path : str, name : str, error : bool) -> int:

    """
    Save data to pickle file
    :param data: data to save
    :param path: path to save
    :param name: name of file
    :return: None
    """

    # check if the types of the variables are the good ones:
    if not isinstance(data, (dict, list, np.ndarray, pd.DataFrame)):
        if error:
            raise TypeError("data must be a dict, list, numpy array or pandas DataFrame")
        else:
            return 3

    if not isinstance(path, str):        
        if error:
            raise TypeError("path must be a string")
        else:
            return 2
    
    if not isinstance(name, str):
        if error:
            raise TypeError("name must be a string")
        else:
            return 1

    # Check if path exist and if not create it
    if not os.path.exists(path):
        os.makedirs(path)

    # Check if the name ends with .pickle
    if not name.endswith('.pickle'):
        name = name + '.pickle'

    # try to save data to pickle file
    with open(path + name, 'wb') as outfile:
        pickle.dump(data, outfile)

    return 0



def load_json(path : str, name : str, error : bool) -> tuple[dict:int]:

    """
    Load data from a json file into a dictionary
    :param path: path to save
    :param name: name of file
    :return: dictionary containing the json data and an code of execution
    """

    # check if the types of the variables are the good ones:
    if not isinstance(path, str):        
        if error:
            raise TypeError("path must be a string")
        else:
            return {}, 2
    
    if not isinstance(name, str):
        if error:
            raise TypeError("name must be a string")
        else:
            return {}, 1

    # Check if path exist and if not create it
    if not os.path.exists(path):
        if error:
            raise FileNotFoundError("The path does not exist")
        else:
            return {}, 3

    # Check if the name ends with .json
    if not name.endswith('.json'):
        name = name + '.json'

    # Check if the file exist
    if not os.path.exists(path + name):
        if error:
            raise FileNotFoundError("The file does not exist")
        else:
            return {}, 4

    # Load data from json file
    with open(path + name, 'r') as infile:
        data = json.load(infile)

    return data, 0



def load_csv(path : str, name : str, error : bool) -> tuple[any:int]:

    """
    Load data from a csv file into a dictionary
    :param path: path to save
    :param name: name of file
    :return: dictionary containing the json data and an code of execution
    """

    # check if the types of the variables are the good ones:
    if not isinstance(path, str):        
        if error:
            raise TypeError("path must be a string")
        else:
            return {}, 2
    
    if not isinstance(name, str):
        if error:
            raise TypeError("name must be a string")
        else:
            return {}, 1

    # Check if path exist and if not create it
    if not os.path.exists(path):
        if error:
            raise FileNotFoundError("The path does not exist")
        else:
            return {}, 3

    # Check if the name ends with .csv
    if not name.endswith('.csv'):
        name = name + '.csv'

    # Check if the file exist
    if not os.path.exists(path + name):
        if error:
            raise FileNotFoundError("The file does not exist")
        else:
            return {}, 4

    # Load data from csv file
    data = pd.read_csv(path + name)

    return data, 0



def load_txt(path : str, name : str, error : bool) -> tuple[any, int]:
    
        """
        Load data from a txt file into a dictionary
        :param path: path to save
        :param name: name of file
        :return: dictionary containing the json data and an code of execution
        """
    
        # check if the types of the variables are the good ones:
        if not isinstance(path, str):        
            if error:
                raise TypeError("path must be a string")
            else:
                return {}, 2
        
        if not isinstance(name, str):
            if error:
                raise TypeError("name must be a string")
            else:
                return {}, 1
    
        # Check if path exist and if not create it
        if not os.path.exists(path):
            if error:
                raise FileNotFoundError("The path does not exist")
            else:
                return {}, 3
    
        # Check if the name ends with .txt
        if not name.endswith('.txt'):
            name = name + '.txt'
    
        # Check if the file exist
        if not os.path.exists(path + name):
            if error:
                raise FileNotFoundError("The file does not exist")
            else:
                return {}, 4
    
        # Load data from txt file
        with open(path + name, 'r') as infile:
            data = infile.read()
    
        return data, 0



def load_pickle(path : str, name : str, error : bool) -> tuple(any, int):

    """
    Load data from a pickle file into a dictionary
    :param path: path to save
    :param name: name of file
    :return: dictionary containing the json data and an code of execution
    """

    # check if the types of the variables are the good ones:
    if not isinstance(path, str):        
        if error:
            raise TypeError("path must be a string")
        else:
            return {}, 2
    
    if not isinstance(name, str):
        if error:
            raise TypeError("name must be a string")
        else:
            return {}, 1

    # Check if path exist and if not create it
    if not os.path.exists(path):
        if error:
            raise FileNotFoundError("The path does not exist")
        else:
            return {}, 3

    # Check if the name ends with .pickle
    if not name.endswith('.pickle'):
        name = name + '.pickle'

    # Check if the file exist
    if not os.path.exists(path + name):
        if error:
            raise FileNotFoundError("The file does not exist")
        else:
            return {}, 4

    # Load data from pickle file
    with open(path + name, 'rb') as infile:
        data = pickle.load(infile)

    return data, 0