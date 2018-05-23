import csv
import operator


class IrysSpecificator(object):
    def __init__(self):
        """
        load sample data and generate characteristics
        for each Irys flower
        """
        self.species = ({
            'setosa': {'sepal_length': [], 'sepal_width': [], 'petal_length': [], 'petal_width': []},
            'versicolor': {'sepal_length': [], 'sepal_width': [], 'petal_length': [], 'petal_width': []},
            'virginica': {'sepal_length': [], 'sepal_width': [], 'petal_length': [], 'petal_width': []}
        })
        self.generate_characteristics()

    def data_csv_reader(self, file_name):
        data_list = []
        with open(file_name, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                data_list.append(row)
        return data_list

    def generate_characteristics(self):
        """
        For each record in sample data check characteristics
        """
        for line in self.data_csv_reader('iris.csv'):

            try:
                self.species[line[4]]['sepal_length'].append(float(line[0]))
                self.species[line[4]]['sepal_width'].append(float(line[1]))
                self.species[line[4]]['petal_length'].append(float(line[2]))
                self.species[line[4]]['petal_width'].append(float(line[3]))
            except (ValueError, KeyError):
                pass

    def get_species(self, sepal_length, sepal_width, petal_length, petal_width):
        """
        recognize the iris species
        """
        try:
            species_points = ({'setosa': 0, 'versicolor': 0, 'virginica': 0})
            for key in ['setosa', 'versicolor', 'virginica']:
                if min(self.species[key]['sepal_length']) < float(sepal_length) < max(self.species[key]['sepal_length']):
                    species_points[key] += 1
                if min(self.species[key]['sepal_width']) < float(sepal_width) < max(self.species[key]['sepal_width']):
                    species_points[key] += 1
                if min(self.species[key]['petal_length']) < float(petal_length) < max(self.species[key]['petal_length']):
                    species_points[key] += 1
                if min(self.species[key]['petal_width']) < float(sepal_length) < max(self.species[key]['petal_width']):
                    species_points[key] += 1
            return max(species_points.iteritems(), key=operator.itemgetter(1))[0]
        except BaseException:
            return 'unable to determine the iris species'


def test():
    specificator = IrysSpecificator()
    species = specificator.get_species('3.1', '3.1', '5.5', '1.8')
    if species == 'virginica':
        print("successfully recognized species ['0', '3.1', '5.5', '1.8'] == virginica")


if __name__ == '__main__':
    test()
