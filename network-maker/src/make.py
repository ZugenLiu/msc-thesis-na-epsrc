#!/usr/bin/env python3

########################################################################################################################

# third-party library modules
import os
from pickle import load
from collections import OrderedDict

########################################################################################################################


# CreateAreaNetwork class
class CreateAreaNetwork:

    @staticmethod
    # runs other functions
    def run():

        # create network in gephi format
        CreateAreaNetwork.create_network('gephi')
        # create network in graphistry format
        CreateAreaNetwork.create_network('graphistry')

    ####################################################################################################################

    # creates network
    @staticmethod
    def create_network(tool):

        # if area nodes in gephi format or edges in graphistry format file does not exist
        if not (os.path.isfile('../../data/networks/areas/nodes_gephi.tsv') and
                os.path.isfile('../../data/networks/areas/edges_graphistry.tsv')):

            # variable to hold input file
            input_file = open(r'../output/areas/info/area_info.pkl', 'rb')
            # load data structure from file
            areas = load(input_file)
            # close input file
            input_file.close()

            # variable to hold input file
            input_file = open(r'../output/areas/links/area_links.pkl', 'rb')
            # load data structure from file
            area_links = load(input_file)
            # close input file
            input_file.close()

            # for area link in area links list
            for area_link in area_links:
                # variable to hold area link swap
                area_link_swap = (area_link[1], area_link[0], area_link[2], area_link[3])
                # remove area link swap from area links list
                area_links.remove(area_link_swap)

            # variable to hold area ids dictionary
            area_ids = OrderedDict()
            # variable to hold identifier set to 1
            identifier = 1
            # for area name in areas dictionary
            for area_name in areas.keys():
                # add identifier to areas ids dictionary
                area_ids[area_name] = identifier
                # increment identifier
                identifier += 1

            # if tool equals to gephi
            if tool == 'gephi':

                # open file
                with open('../../data/networks/areas/nodes_gephi.tsv', 'w') as output_file:
                    # write headers to file
                    output_file.write('Id\tLabel\tGrantNum\tPropVal\tGrantVal\n')
                    # for area name and id in areas ids dictionary
                    for area_name, area_id in area_ids.items():
                        # variable to hold area grant number
                        area_grant_num = areas.get(area_name)[1]
                        # variable to hold area proportional value
                        area_prop_val = areas.get(area_name)[2]
                        # variable to hold area grant value
                        area_grant_val = areas.get(area_name)[3]
                        # write area to file
                        output_file.write('{}\t{}\t{}\t{}\t{}\n'.format(area_id, area_name, area_grant_num,
                                                                        area_prop_val, area_grant_val))

                # variable to hold output file
                with open('../../data/networks/areas/edges_gephi.tsv', 'w') as output_file:
                    # write headers to file
                    output_file.write('Source\tTarget\tType\tWeight\tTotalVal\n')
                    # for area link in area links dictionary
                    for area_link in area_links:
                        # variable to hold first area name
                        area_name_1st = area_link[0]
                        # variable to hold first area id
                        area_id_1st = area_ids.get(area_name_1st)
                        # variable to hold second area name
                        area_name_2nd = area_link[1]
                        # variable to hold second area id
                        area_id_2nd = area_ids.get(area_name_2nd)
                        # write area link to file
                        output_file.write('{}\t{}\t{}\t{:.1f}\t{}\n'.format(area_id_1st, area_id_2nd, 'Undirected',
                                                                            area_link[2], area_link[3]))

                # print progress
                print('> Creation of Area Network in Gephi format completed')

            # if tool equals to graphistry
            elif tool == 'graphistry':
                # variable to hold output file
                with open('../../data/networks/areas/edges_graphistry.tsv', 'w') as output_file:
                    # write headers to file
                    output_file.write('source\ttarget\tvalue\n')
                    # for area link in area links dictionary
                    for area_link in area_links:
                        # write area link to file
                        output_file.write('{}\t{}\t{}\n'.format(area_link[0], area_link[1], area_link[2]))

                # print progress
                print('> Creation of Area Network in Graphistry format completed')


########################################################################################################################


# CreateTopicNetwork class
class CreateTopicNetwork:

    @staticmethod
    # runs other functions
    def run():

        # create network a
        CreateTopicNetwork.create_network_a()
        # create network b
        CreateTopicNetwork.create_network_b()

    ####################################################################################################################

    @staticmethod
    # creates network a
    def create_network_a():

        # if topic nodes in gephi format file does not exist
        if not os.path.isfile('../../data/networks/topics/network-a/nodes_gephi.tsv'):

            # variable to hold input file
            input_file = open(r'../output/topics/info/grants/grant_topic_info.pkl', 'rb')
            # load data structure from file
            topics = load(input_file)
            # close input file
            input_file.close()

            # variable to hold input file
            input_file = open(r'../output/topics/links/grant_topic_links.pkl', 'rb')
            # load data structure from file
            topic_links = load(input_file)
            # close input file
            input_file.close()

            # variables to hold topic ids and identifier set to 1
            topic_ids, identifier = OrderedDict(), 1
            # for topic name in topics
            for topic_name in topics.keys():
                # add identifier to topic ids
                topic_ids[topic_name] = identifier
                # increment identifier
                identifier += 1

            # variable to hold output file
            output_file = open('../../data/networks/topics/network-a/nodes_gephi.tsv', 'w')
            # write headers to file
            output_file.write('Id\tLabel\tNum\tVal\n')
            # for topic name and id in topic ids
            for topic_name, topic_id in topic_ids.items():
                # variables to hold number and value
                number, value = topics.get(topic_name)[0], topics.get(topic_name)[1]
                # write topic to file
                output_file.write('{}\t{}\t{}\t{}\t\n'.format(topic_id, topic_name, number, value))

            # variable to hold output file
            output_file = open('../../data/networks/topics/network-a/edges_gephi.tsv', 'w')
            # write headers to file
            output_file.write('Source\tTarget\tType\tWeight\tVal\n')
            # for topic link in topic links
            for topic_link in topic_links:
                # variable to hold source
                source = topic_link[0]
                # variable to hold source id
                source_id = topic_ids.get(source)
                # variable to hold target
                target = topic_link[1]
                # variable to hold target id
                target_id = topic_ids.get(target)
                # write topic link to file
                output_file.write('{}\t{}\t{}\t{:.1f}\t{}\n'.format(source_id, target_id, 'Undirected', topic_link[2],
                                                                    topic_link[3]))

            # print progress
            print('> Creation of Topic Network A in Gephi format completed')

    ####################################################################################################################

    @staticmethod
    # creates network b
    def create_network_b():

        # if topic nodes in gephi format file does not exist
        if not os.path.isfile('../../data/networks/topics/network-b/nodes_gephi.tsv'):

            # variable to hold input file
            input_file = open(r'../output/topics/info/researchers/researcher_topic_info.pkl', 'rb')
            # load data structure from file
            topics = load(input_file)
            # close input file
            input_file.close()

            # variable to hold input file
            input_file = open(r'../output/topics/links/researcher_topic_links.pkl', 'rb')
            # load data structure from file
            topic_links = load(input_file)
            # close input file
            input_file.close()

            # variables to hold topic ids and identifier set to 1
            topic_ids, identifier = OrderedDict(), 1
            # for topic name in topics
            for topic_name in topics.keys():
                # add identifier to topic ids
                topic_ids[topic_name] = identifier
                # increment identifier
                identifier += 1

            # variable to hold output file
            output_file = open('../../data/networks/topics/network-b/nodes_gephi.tsv', 'w')
            # write headers to file
            output_file.write('Id\tLabel\tNum\n')
            # for topic name and id in topic ids
            for topic_name, topic_id in topic_ids.items():
                # variables to hold number
                number = topics.get(topic_name)
                # write topic to file
                output_file.write('{}\t{}\t{}\n'.format(topic_id, topic_name, number))

            # variable to hold output file
            output_file = open('../../data/networks/topics/network-b/edges_gephi.tsv', 'w')
            # write headers to file
            output_file.write('Source\tTarget\tType\tWeight\n')
            # for topic link in topic links
            for topic_link in topic_links:
                # variable to hold source
                source = topic_link[0]
                # variable to hold source id
                source_id = topic_ids.get(source)
                # variable to hold target
                target = topic_link[1]
                # variable to hold target id
                target_id = topic_ids.get(target)
                # write topic link to file
                output_file.write('{}\t{}\t{}\t{:.1f}\n'.format(source_id, target_id, 'Undirected', topic_link[2]))

            # print progress
            print('> Creation of Topic Network B in Gephi format completed')


########################################################################################################################


# CreateResearcherNetwork class
class CreateResearcherNetwork:

    @staticmethod
    # runs other functions
    def run():

        # create network a
        CreateResearcherNetwork.create_network_a()
        # create network b
        CreateResearcherNetwork.create_network_b()

    ####################################################################################################################

    @staticmethod
    # creates network a
    def create_network_a():
        pass

    ####################################################################################################################

    @staticmethod
    # creates network b
    def create_network_b():
        pass


########################################################################################################################


# CreatePastTopicNetwork class
class CreatePastTopicNetwork:

    @staticmethod
    # runs other functions
    def run():

        # create network a
        CreatePastTopicNetwork.create_network_a('_1990_2000')
        # create network a
        CreatePastTopicNetwork.create_network_a('_2000_2010')

        # create network b
        CreatePastTopicNetwork.create_network_b('_1990_2000')
        # create network b
        CreatePastTopicNetwork.create_network_b('_2000_2010')

    ####################################################################################################################

    @staticmethod
    # creates network a
    def create_network_a(years):

        # if topic nodes in gephi format file does not exist
        if not os.path.isfile('../../data/networks/past-topics/network-a/nodes_gephi{}.tsv'.format(years)):

            # variable to hold input file
            input_file = open(r'../output/past-topics/info/grants/grant_topic_info{}.pkl'.format(years), 'rb')
            # load data structure from file
            topics = load(input_file)
            # close input file
            input_file.close()

            # variable to hold input file
            input_file = open(r'../output/past-topics/links/grant_topic_links{}.pkl'.format(years), 'rb')
            # load data structure from file
            topic_links = load(input_file)
            # close input file
            input_file.close()

            # variables to hold topic ids and identifier set to 1
            topic_ids, identifier = OrderedDict(), 1
            # for topic name in topics
            for topic_name in topics.keys():
                # add identifier to topic ids
                topic_ids[topic_name] = identifier
                # increment identifier
                identifier += 1

            # variable to hold output file
            output_file = open('../../data/networks/past-topics/network-a/nodes_gephi{}.tsv'.format(years), 'w')
            # write headers to file
            output_file.write('Id\tLabel\tNum\tVal\n')
            # for topic name and id in topic ids
            for topic_name, topic_id in topic_ids.items():
                # variables to hold number and value
                number, value = topics.get(topic_name)[0], topics.get(topic_name)[1]
                # write topic to file
                output_file.write('{}\t{}\t{}\t{}\t\n'.format(topic_id, topic_name, number, value))

            # variable to hold output file
            output_file = open('../../data/networks/past-topics/network-a/edges_gephi{}.tsv'.format(years), 'w')
            # write headers to file
            output_file.write('Source\tTarget\tType\tWeight\tVal\n')
            # for topic link in topic links
            for topic_link in topic_links:
                # variable to hold source
                source = topic_link[0]
                # variable to hold source id
                source_id = topic_ids.get(source)
                # variable to hold target
                target = topic_link[1]
                # variable to hold target id
                target_id = topic_ids.get(target)
                # write topic link to file
                output_file.write('{}\t{}\t{}\t{:.1f}\t{}\n'.format(source_id, target_id, 'Undirected', topic_link[2],
                                                                    topic_link[3]))

            # print progress
            print('> Creation of Past Topic Network A ({}) in Gephi format completed'
                  .format(years[1:].replace('_', '-')))

    ####################################################################################################################

    @staticmethod
    # creates network b
    def create_network_b(years):

        # if topic nodes in gephi format file does not exist
        if not os.path.isfile('../../data/networks/past-topics/network-b/nodes_gephi{}.tsv'.format(years)):

            # variable to hold input file
            input_file = open(r'../output/past-topics/info/researchers/researcher_topic_info{}.pkl'.format(years), 'rb')
            # load data structure from file
            topics = load(input_file)
            # close input file
            input_file.close()

            # variable to hold input file
            input_file = open(r'../output/past-topics/links/researcher_topic_links{}.pkl'.format(years), 'rb')
            # load data structure from file
            topic_links = load(input_file)
            # close input file
            input_file.close()

            # variables to hold topic ids and identifier set to 1
            topic_ids, identifier = OrderedDict(), 1
            # for topic name in topics
            for topic_name in topics.keys():
                # add identifier to topic ids
                topic_ids[topic_name] = identifier
                # increment identifier
                identifier += 1

            # variable to hold output file
            output_file = open('../../data/networks/past-topics/network-b/nodes_gephi{}.tsv'.format(years), 'w')
            # write headers to file
            output_file.write('Id\tLabel\tNum\n')
            # for topic name and id in topic ids
            for topic_name, topic_id in topic_ids.items():
                # variables to hold number
                number = topics.get(topic_name)
                # write topic to file
                output_file.write('{}\t{}\t{}\n'.format(topic_id, topic_name, number))

            # variable to hold output file
            output_file = open('../../data/networks/past-topics/network-b/edges_gephi{}.tsv'.format(years), 'w')
            # write headers to file
            output_file.write('Source\tTarget\tType\tWeight\n')
            # for topic link in topic links
            for topic_link in topic_links:
                # variable to hold source
                source = topic_link[0]
                # variable to hold source id
                source_id = topic_ids.get(source)
                # variable to hold target
                target = topic_link[1]
                # variable to hold target id
                target_id = topic_ids.get(target)
                # write topic link to file
                output_file.write('{}\t{}\t{}\t{:.1f}\n'.format(source_id, target_id, 'Undirected', topic_link[2]))

            # print progress
            print('> Creation of Past Topic Network B ({}) in Gephi format completed'
                  .format(years[1:].replace('_', '-')))


########################################################################################################################


# CreatePastResearcherNetwork class
class CreatePastResearcherNetwork:

    @staticmethod
    def run():

        # create network a
        CreatePastResearcherNetwork.create_network_a('')
        # create network a
        CreatePastResearcherNetwork.create_network_a('')

        # create network b
        CreatePastResearcherNetwork.create_network_b('')
        # create network b
        CreatePastResearcherNetwork.create_network_b('')

    ####################################################################################################################

    @staticmethod
    # creates network a
    def create_network_a(years):
        pass

    ####################################################################################################################

    @staticmethod
    # creates network b
    def create_network_b(years):
        pass


########################################################################################################################


# main function
def main():

    # create area network
    CreateAreaNetwork.run()

    # create topic network
    CreateTopicNetwork.run()
    # create researcher network
    CreateResearcherNetwork.run()

    # create past topic network
    CreatePastTopicNetwork.run()
    # create past researcher network
    CreatePastResearcherNetwork.run()


########################################################################################################################


# runs main function
if __name__ == '__main__':
    main()


########################################################################################################################
