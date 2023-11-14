from RGB import *
from temperatures import *
from PIL import Image
import time
import os

# Learning
# # Opening
start_learning = cv.imread('frame1.png')
wanted_learning = cv.imread('frame1_pyro.png')

# # Setting the right format
start_learning = cv.cvtColor(start_learning, cv.COLOR_BGR2RGB)
wanted_learning = cv.cvtColor(wanted_learning, cv.COLOR_BGR2RGB)
start_learning = shape_change(start_learning)   # Deleting axis
wanted_learning = shape_change(wanted_learning)
start_learning = blue_removal(start_learning)

# # Learning, creation of the matrix RGB pyro/actual
start_learn = time.perf_counter()
transfer_matrix = transfer_matrix_creation(start_learning, wanted_learning)
end_learn = time.perf_counter()


# Proper functioning test
# # Opening
fluctual = r"C:\Users\marie\PycharmProjects\2nd_essai\Images_fluctual"
started = os.path.join(fluctual, 'Actual', 'frame2.png')
wanted = os.path.join(fluctual, 'Pyro', 'frame2.png')
start = cv.imread(started)
wanted = cv.imread(wanted)

# # Setting the right format
start_ttmt_pix = time.perf_counter()
start = cv.cvtColor(start, cv.COLOR_BGR2RGB)
wanted = cv.cvtColor(wanted, cv.COLOR_BGR2RGB)
start = blue_removal(start)

# # Treatment
# # # Converting actual into pyrometric
treated_pyro = treatment1_tot(start, transfer_matrix)
end_ttmt_pix = time.perf_counter()
# # # Converting pyrometric into temperature
start_ttmt_temp = time.perf_counter()
treated_temp = temperature_matrix(transfo_temperature, treated_pyro)
end_ttmt_temp = time.perf_counter()
wanted_temp = temperature_matrix(transfo_temperature, wanted)

# # Error calculations
size = treated_pyro.shape
nb_tot_pix = size[0]*size[1]
nb_wrong_pix_tol_0 = differences(treated_pyro, wanted)
wrong_percentage = nb_wrong_pix_tol_0*100/nb_tot_pix
print("Number of poorly processed pixels: ", nb_wrong_pix_tol_0, "/", nb_tot_pix, "or", wrong_percentage, "%")


tolerances_list = [3, 5, 7, 10, 15, 20]
for i in tolerances_list:
    nb_wrong_pix = differences_tol(i, treated_pyro, wanted)
    percent = nb_wrong_pix*100/nb_tot_pix
    print("Number of poorly processed pixels, tolerance", i, ": ", nb_wrong_pix, "/", nb_tot_pix, "or", percent, "%")


right, less_5, from5to10, from10to15, from15to20, more_20 = temperature_difference(treated_temp, wanted_temp)
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


# # Treatment time calculation
learning_time = end_learn - start_learn
ttmt_pix_time = end_ttmt_pix - start_ttmt_pix
ttmt_temp_time = end_ttmt_temp - start_ttmt_temp
print("learning_time: ", learning_time)
print("ttmt_pix_time: ", ttmt_pix_time)
print("ttmt_temp_time: ", ttmt_temp_time)

treated_pyro = treated_pyro.astype(np.uint8)
image = Image.fromarray(treated_pyro)
image.save('treated_RGB_normal.png')
image.show()
