def log_analyzer(file_name):
    log_dictionary = {
        'ERROR': [],
        'WARNING': [],
        'INFO': []
    }

    try:
        with open(file_name, 'r') as log_file:
            lines = log_file.readlines()

        for line in lines:
            if 'ERROR' in line:
                log_dictionary['ERROR'].append(line.strip())
            elif 'WARNING' in line:
                log_dictionary['WARNING'].append(line.strip())
            elif 'INFO' in line:
                log_dictionary['INFO'].append(line.strip())

        return log_dict

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    log_file_name = 'server_logs.txt'
    result = log_analyzer(log_file_name)

    if result is not None:
        print("Log Analysis Report:")
        for key, value in result.items():
            print(f"{key}: {value}")
