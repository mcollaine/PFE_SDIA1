from couleur_cluster import *
from temp import *
import cv2 as cv
import time
import matplotlib.pyplot as plt
import operator as op



# Learning
# # Opening
start_learning = cv.imread('frame1.png')
wanted_learning = cv.imread('frame1_pyro.png')

# # Setting the right format
start_learning = shape_change(start_learning)
wanted_learning = shape_change(wanted_learning)
start_learning = cv.cvtColor(start_learning, cv.COLOR_BGR2RGB)
wanted_learning = cv.cvtColor(wanted_learning, cv.COLOR_BGR2RGB)

# # Création de la matrice de transformation
start_learn = time.perf_counter()
transfer_matrix = transfer_matrix_creation(start_learning, wanted_learning)
end_learn = time.perf_counter()




# Proper functioning test
# # Opening
start = cv.imread('frame2.png')
wanted = cv.imread('frame2_pyro.png')

# # Setting the right fomat
start = cv.cvtColor(start, cv.COLOR_BGR2RGB)
wanted = cv.cvtColor(wanted, cv.COLOR_BGR2RGB)
start = shape_change(start)
wanted = shape_change(wanted)
size = start.shape
start = start.reshape((-1, 3))
# start_without_blue = flattening_mat(start)
# wanted_without_blue = flattening_mat(wanted)


# # Clustering
n = 50 # Nnumber of clustering
start_clus = time.perf_counter()
centroids, start_labels = clustering(n, start)  # or start
end_clus = time.perf_counter()

# # Reconstitution of the pyrometric image thanks to the clusters of the actual flame image
start_transfo = time.perf_counter()
centroids = normalization(centroids)
pyro_centroids = treatment_tot(transfer_matrix, centroids)
pyro_treated = label_values_allocation(pyro_centroids, start_labels)
pyro_treated = matrix_volume_setting(size, pyro_treated)
end_transfo = time.perf_counter()

# # Converting clusters image into temperature
centroids_temperatures = temperature_centroid(transfo_temperature, pyro_centroids) # centroids pixels transformés en températures
temp_treated = label_values_allocation(centroids_temperatures, start_labels)
temp_treated = matrix_volume_setting(size, temp_treated)
temp_wanted = matrix_temperature(transfo_temperature, wanted)



# # Calculations time
time_learning = end_learn - start_learn
time_clus = end_clus - start_clus
time_transfo = end_transfo - start_transfo

print("Learning time: ", time_learning)
print("Clustering time: ", time_clus)
print("Transformation time: ", time_transfo)


# # Error calculations
nb_tot_pix = size[0]*size[1]
print("Number of clusters: ", n)



tolerances_list = [0, 3, 5, 7, 10, 15, 20]
for i in tolerances_list:
    nb_wrong_pix = differences_tol(i, pyro_treated, wanted)
    percent = nb_wrong_pix*100/nb_tot_pix
    print("Number of poorly processed pixels, tolerance", i, ": ", nb_wrong_pix, "/", nb_tot_pix, "or", percent, "%")

right, less_5, from5to10, from10to15, from15to20, more_20 = difference_temperature(temp_treated, temp_wanted)
percentage_right_temp = right*100/nb_tot_pix
print("Number of right processed temperatures: ", right, "/", nb_tot_pix, "or", percentage_right_temp, "%")
temp_gap_inf_5 = less_5*100/nb_tot_pix
print("Degrees  difference less than 5K: ", less_5, "/", nb_tot_pix, "or", temp_gap_inf_5, "%")
temp_gap_between_5and10 = from5to10*100/nb_tot_pix
print("Degrees difference between 5 and 10K: ", from5to10, "/", nb_tot_pix, "or", temp_gap_between_5and10, "%")
temp_gap_between_10and15 = from10to15*100/nb_tot_pix
print("Degrees difference between 10 and 15K: ", from10to15, "/", nb_tot_pix, "or", temp_gap_between_10and15, "%")
temp_gap_between_15and20 = from15to20*100/nb_tot_pix
print("Degrees difference between 15 and 20K: ", from15to20,  "/", nb_tot_pix, "or", temp_gap_between_15and20, "%")
temp_gap_sup_20 = more_20*100/nb_tot_pix
print("Degrees difference more than 20K: ", more_20, "/", nb_tot_pix, "or", temp_gap_sup_20, "%")

