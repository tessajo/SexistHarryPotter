

    '''
    for key in connection_f:
        value = connection_f.get(key)
        g_f.add_node(key[0], cluster='noun')
        g_f.add_node(key[1], cluster='ad')
        g_f.add_edge(key[0],key[1],weight=value)
        weight_of_nodes.append(value)
        # Color-Mapping
        if key[1] in fv_names: # Paar aus Namen
            # Name 1 bereits erfasst?
            if not key[0] in l_of_names: # Wenn nein
                color_map.append(dgreen) # TODO Farbe ändern
                l_of_names.append(key[0])
            # Name 2 bereits erfasst?
            if not key[1] in l_of_names: # Wenn nein
                color_map.append(dgreen)
                l_of_names.append(key[1])
        else: # nur 1 Name
            if not key[0] in l_of_names:
                color_map.append(dgreen)
                l_of_names.append(key[0])
            #Color-Mapping für alle anderen Wörter
            if not key[1] in l_of_words: 
                color_map.append(lblue)
                l_of_words.append(key[1])
    # assortativity_coefficient
    cr_f = nx.attribute_assortativity_coefficient(g_f,"cluster",nodes=key)
    rec_f = nx.overall_reciprocity(g_f)
    print(cr_f, rec_f)
    # Kennzahlen & Algos
    # print(weight_of_nodes)
    fig = plt.figure(figsize= (50,20))
    subax1 = plt.subplot(122)
    nx.draw(g_f, node_color=color_map, edge_color ='grey', with_labels=True)
    subax1.set_title(f"Wortverknüpfungen der weiblichen Personen\nAssortivitätskoeffizient: {cr_f}\nReciprocity: {rec_f}")
    # plt.savefig('wordconnectivity_women.png')
    # Männer-Graph
    color_map = []
    l_of_names = []
    l_of_words = []
    weight_of_nodes = []
    for key in connection_m:
        value = connection_m.get(key)
        g_m.add_node(key[0], cluster='noun', color='red')
        g_m.add_node(key[1], cluster='ad', color='red')
        g_m.add_edge(key[0],key[1],weight=value)
        weight_of_nodes.append(value)
    # Color-Mapping
        if key[1] in fv_names: # Paar aus Namen
            # Name 1 bereits erfasst?
            if not key[0] in l_of_names: # Wenn nein
                color_map.append(dgreen)
                l_of_names.append(key[0])
            # Name 2 bereits erfasst?
            if not key[1] in l_of_names: # Wenn nein
                color_map.append(dgreen)
                l_of_names.append(key[1])
        else: # nur 1 Name
            if not key[0] in l_of_names:
                color_map.append(dgreen)
                l_of_names.append(key[0])
            #Color-Mapping für alle anderen Wörter
            if not key[1] in l_of_words: 
                color_map.append(lblue)
                l_of_words.append(key[1])
    # assortativity_coefficient
    cr_m = nx.attribute_assortativity_coefficient(g_m,"cluster",nodes=key)
    rec_m = nx.overall_reciprocity(g_m)
    print(cr_m, rec_m)
    # Kennzahlen & Algos
    # print(weight_of_nodes)
    fig = plt.figure(figsize= (50,20))
    subax1 = plt.subplot(122)
    nx.draw(g_m, node_color=color_map, edge_color ='grey', with_labels=True)
    subax1.set_title(f"Wortverknüpfungen der männlichen Personen\nAssortivitätskoeffizient: {cr_m}\nReciprocity: {rec_m}")
    # plt.savefig('wordconnectivity_men.png')

    
'''