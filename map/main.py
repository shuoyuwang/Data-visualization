from get_data import Get_data
import execution

if __name__ == '__main__':
    data = Get_data()
    data.get_data()

    time_in, time_out = data.get_time()
    data.parse_data()

    execution.china_map(time_in)
    execution.province_map(time_in)


