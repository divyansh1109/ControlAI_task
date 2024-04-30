import csv
from pandas import *


class WarehouseParcelDetail:
    def __init__(self, parcel_number, parcel_weight, parcel_category):
        self.parcel_number = parcel_number
        self.parcel_weight = parcel_weight
        self.parcel_category = parcel_category

    def save_parcel_details(self):

        with open('parcel_details.csv', 'a', newline='') as csvfile:
            fieldnames = ['filters', 'automobile_parts', 'cargo_container']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            if self.parcel_category == 'filters':
                writer.writerow({'filters': self.parcel_number})
            elif self.parcel_category == 'automobile_parts':
                writer.writerow({'automobile_parts': self.parcel_number})
            elif self.parcel_category == 'cargo_container':
                writer.writerow({'cargo_container': self.parcel_number})
            else:
                print("Category not defined!")

    def display_details(self):

        data = read_csv('parcel_details.csv')
        filters_data = data['filters'].tolist()
        auto_data = data['automobile_parts'].tolist()
        cargo_data = data['cargo_container'].tolist()
        print('filters:', filters_data)
        print('auto_data:', auto_data)
        print('cargo_data:', cargo_data)


parcel1 = WarehouseParcelDetail("23456", 10, "filters")
parcel2 = WarehouseParcelDetail("96355", 10, "filters")
parcel3 = WarehouseParcelDetail("83722", 10, "filters")
parcel4 = WarehouseParcelDetail("66234", 14, "automobile_parts")
parcel5 = WarehouseParcelDetail("86643", 14, "automobile_parts")
parcel6 = WarehouseParcelDetail("64326", 14, "automobile_parts")
parcel7 = WarehouseParcelDetail("98432", 16, "cargo_container")
parcel8 = WarehouseParcelDetail("53463", 16, "cargo_container")
parcel9 = WarehouseParcelDetail("87653", 16, "cargo_container")

parcel1.save_parcel_details()
parcel2.save_parcel_details()
parcel3.save_parcel_details()
parcel4.save_parcel_details()
parcel5.save_parcel_details()
parcel6.save_parcel_details()
parcel7.save_parcel_details()
parcel8.save_parcel_details()
parcel9.save_parcel_details()

parcel9.display_details()