import secrets
import Common
from Common import createFolder, path
from passlib.hash import argon2


with open(f'{path}/prime_50000', 'r') as f:
    primes = f.read().split(",")

num = secrets.randbelow(20000)

a_l1, a_l2, a_l3, a_l4, a_l5, a_l6, a_l7, a_l8, a_l9, a_l10, a_l11, a_l12, a_l13, a_l14, a_l15 = primes[num:num + 15]
b_l1, b_l2, b_l3, b_l4, b_l5, b_l6, b_l7, b_l8, b_l9, b_l10, b_l11, b_l12, b_l13, b_l14, b_l15 = primes[num + 15:num + 30]
c_l1, c_l2, c_l3, c_l4, c_l5, c_l6, c_l7, c_l8, c_l9, c_l10, c_l11, c_l12, c_l13, c_l14, c_l15 = primes[num + 30:num + 45]
d_l1, d_l2, d_l3, d_l4, d_l5, d_l6, d_l7, d_l8, d_l9, d_l10, d_l11, d_l12, d_l13, d_l14, d_l15 = primes[num + 45:num + 60]
e_l1, e_l2, e_l3, e_l4, e_l5, e_l6, e_l7, e_l8, e_l9, e_l10, e_l11, e_l12, e_l13, e_l14, e_l15 = primes[num + 60:num + 75]
f_l1, f_l2, f_l3, f_l4, f_l5, f_l6, f_l7, f_l8, f_l9, f_l10, f_l11, f_l12, f_l13, f_l14, f_l15 = primes[num + 75:num + 90]
g_l1, g_l2, g_l3, g_l4, g_l5, g_l6, g_l7, g_l8, g_l9, g_l10, g_l11, g_l12, g_l13, g_l14, g_l15 = primes[num + 90:num + 105]
h_l1, h_l2, h_l3, h_l4, h_l5, h_l6, h_l7, h_l8, h_l9, h_l10, h_l11, h_l12, h_l13, h_l14, h_l15 = primes[num + 105:num + 120]
i_l1, i_l2, i_l3, i_l4, i_l5, i_l6, i_l7, i_l8, i_l9, i_l10, i_l11, i_l12, i_l13, i_l14, i_l15 = primes[num + 120:num + 135]
j_l1, j_l2, j_l3, j_l4, j_l5, j_l6, j_l7, j_l8, j_l9, j_l10, j_l11, j_l12, j_l13, j_l14, j_l15 = primes[num + 135:num + 150]
k_l1, k_l2, k_l3, k_l4, k_l5, k_l6, k_l7, k_l8, k_l9, k_l10, k_l11, k_l12, k_l13, k_l14, k_l15 = primes[num + 150:num + 165]
l_l1, l_l2, l_l3, l_l4, l_l5, l_l6, l_l7, l_l8, l_l9, l_l10, l_l11, l_l12, l_l13, l_l14, l_l15 = primes[num + 165:num + 180]
m_l1, m_l2, m_l3, m_l4, m_l5, m_l6, m_l7, m_l8, m_l9, m_l10, m_l11, m_l12, m_l13, m_l14, m_l15 = primes[num + 180:num + 195]
n_l1, n_l2, n_l3, n_l4, n_l5, n_l6, n_l7, n_l8, n_l9, n_l10, n_l11, n_l12, n_l13, n_l14, n_l15 = primes[num + 195:num + 210]
o_l1, o_l2, o_l3, o_l4, o_l5, o_l6, o_l7, o_l8, o_l9, o_l10, o_l11, o_l12, o_l13, o_l14, o_l15 = primes[num + 210:num + 225]
p_l1, p_l2, p_l3, p_l4, p_l5, p_l6, p_l7, p_l8, p_l9, p_l10, p_l11, p_l12, p_l13, p_l14, p_l15 = primes[num + 225:num + 240]
q_l1, q_l2, q_l3, q_l4, q_l5, q_l6, q_l7, q_l8, q_l9, q_l10, q_l11, q_l12, q_l13, q_l14, q_l15 = primes[num + 240:num + 255]
r_l1, r_l2, r_l3, r_l4, r_l5, r_l6, r_l7, r_l8, r_l9, r_l10, r_l11, r_l12, r_l13, r_l14, r_l15 = primes[num + 255:num + 270]
s_l1, s_l2, s_l3, s_l4, s_l5, s_l6, s_l7, s_l8, s_l9, s_l10, s_l11, s_l12, s_l13, s_l14, s_l15 = primes[num + 270:num + 285]
t_l1, t_l2, t_l3, t_l4, t_l5, t_l6, t_l7, t_l8, t_l9, t_l10, t_l11, t_l12, t_l13, t_l14, t_l15 = primes[num + 285:num + 300]
u_l1, u_l2, u_l3, u_l4, u_l5, u_l6, u_l7, u_l8, u_l9, u_l10, u_l11, u_l12, u_l13, u_l14, u_l15 = primes[num + 300:num + 315]
v_l1, v_l2, v_l3, v_l4, v_l5, v_l6, v_l7, v_l8, v_l9, v_l10, v_l11, v_l12, v_l13, v_l14, v_l15 = primes[num + 315:num + 330]
w_l1, w_l2, w_l3, w_l4, w_l5, w_l6, w_l7, w_l8, w_l9, w_l10, w_l11, w_l12, w_l13, w_l14, w_l15 = primes[num + 330:num + 345]
x_l1, x_l2, x_l3, x_l4, x_l5, x_l6, x_l7, x_l8, x_l9, x_l10, x_l11, x_l12, x_l13, x_l14, x_l15 = primes[num + 345:num + 360]
y_l1, y_l2, y_l3, y_l4, y_l5, y_l6, y_l7, y_l8, y_l9, y_l10, y_l11, y_l12, y_l13, y_l14, y_l15 = primes[num + 360:num + 375]
z_l1, z_l2, z_l3, z_l4, z_l5, z_l6, z_l7, z_l8, z_l9, z_l10, z_l11, z_l12, z_l13, z_l14, z_l15 = primes[num + 375:num + 390]
l_0_1, l_0_2, l_0_3, l_0_4, l_0_5, l_0_6, l_0_7, l_0_8, l_0_9, l_0_10, l_0_11, l_0_12, l_0_13, l_0_14, l_0_15 = primes[num + 405:num + 420]
l_1_1, l_1_2, l_1_3, l_1_4, l_1_5, l_1_6, l_1_7, l_1_8, l_1_9, l_1_10, l_1_11, l_1_12, l_1_13, l_1_14, l_1_15 = primes[num + 420:num + 435]
l_2_1, l_2_2, l_2_3, l_2_4, l_2_5, l_2_6, l_2_7, l_2_8, l_2_9, l_2_10, l_2_11, l_2_12, l_2_13, l_2_14, l_2_15 = primes[num + 435:num + 450]
l_3_1, l_3_2, l_3_3, l_3_4, l_3_5, l_3_6, l_3_7, l_3_8, l_3_9, l_3_10, l_3_11, l_3_12, l_3_13, l_3_14, l_3_15 = primes[num + 450:num + 465]
l_4_1, l_4_2, l_4_3, l_4_4, l_4_5, l_4_6, l_4_7, l_4_8, l_4_9, l_4_10, l_4_11, l_4_12, l_4_13, l_4_14, l_4_15 = primes[num + 465:num + 480]
l_5_1, l_5_2, l_5_3, l_5_4, l_5_5, l_5_6, l_5_7, l_5_8, l_5_9, l_5_10, l_5_11, l_5_12, l_5_13, l_5_14, l_5_15 = primes[num + 480:num + 495]
l_6_1, l_6_2, l_6_3, l_6_4, l_6_5, l_6_6, l_6_7, l_6_8, l_6_9, l_6_10, l_6_11, l_6_12, l_6_13, l_6_14, l_6_15 = primes[num + 495:num + 510]
l_7_1, l_7_2, l_7_3, l_7_4, l_7_5, l_7_6, l_7_7, l_7_8, l_7_9, l_7_10, l_7_11, l_7_12, l_7_13, l_7_14, l_7_15 = primes[num + 510:num + 525]
l_8_1, l_8_2, l_8_3, l_8_4, l_8_5, l_8_6, l_8_7, l_8_8, l_8_9, l_8_10, l_8_11, l_8_12, l_8_13, l_8_14, l_8_15 = primes[num + 525:num + 540]
l_9_1, l_9_2, l_9_3, l_9_4, l_9_5, l_9_6, l_9_7, l_9_8, l_9_9, l_9_10, l_9_11, l_9_12, l_9_13, l_9_14, l_9_15 = primes[num + 540:num + 555]
A_l1, A_l2, A_l3, A_l4, A_l5, A_l6, A_l7, A_l8, A_l9, A_l10, A_l11, A_l12, A_l13, A_l14, A_l15 = primes[
                                                                                                 num + 570:num + 585]
B_l1, B_l2, B_l3, B_l4, B_l5, B_l6, B_l7, B_l8, B_l9, B_l10, B_l11, B_l12, B_l13, B_l14, B_l15 = primes[
                                                                                                 num + 585:num + 600]
C_l1, C_l2, C_l3, C_l4, C_l5, C_l6, C_l7, C_l8, C_l9, C_l10, C_l11, C_l12, C_l13, C_l14, C_l15 = primes[
                                                                                                 num + 600:num + 615]
D_l1, D_l2, D_l3, D_l4, D_l5, D_l6, D_l7, D_l8, D_l9, D_l10, D_l11, D_l12, D_l13, D_l14, D_l15 = primes[
                                                                                                 num + 615:num + 630]
E_l1, E_l2, E_l3, E_l4, E_l5, E_l6, E_l7, E_l8, E_l9, E_l10, E_l11, E_l12, E_l13, E_l14, E_l15 = primes[
                                                                                                 num + 630:num + 645]
F_l1, F_l2, F_l3, F_l4, F_l5, F_l6, F_l7, F_l8, F_l9, F_l10, F_l11, F_l12, F_l13, F_l14, F_l15 = primes[
                                                                                                 num + 645:num + 660]
G_l1, G_l2, G_l3, G_l4, G_l5, G_l6, G_l7, G_l8, G_l9, G_l10, G_l11, G_l12, G_l13, G_l14, G_l15 = primes[
                                                                                                 num + 660:num + 675]
H_l1, H_l2, H_l3, H_l4, H_l5, H_l6, H_l7, H_l8, H_l9, H_l10, H_l11, H_l12, H_l13, H_l14, H_l15 = primes[
                                                                                                 num + 675:num + 690]
I_l1, I_l2, I_l3, I_l4, I_l5, I_l6, I_l7, I_l8, I_l9, I_l10, I_l11, I_l12, I_l13, I_l14, I_l15 = primes[
                                                                                                 num + 690:num + 705]
J_l1, J_l2, J_l3, J_l4, J_l5, J_l6, J_l7, J_l8, J_l9, J_l10, J_l11, J_l12, J_l13, J_l14, J_l15 = primes[
                                                                                                 num + 705:num + 720]
K_l1, K_l2, K_l3, K_l4, K_l5, K_l6, K_l7, K_l8, K_l9, K_l10, K_l11, K_l12, K_l13, K_l14, K_l15 = primes[
                                                                                                 num + 720:num + 735]
L_l1, L_l2, L_l3, L_l4, L_l5, L_l6, L_l7, L_l8, L_l9, L_l10, L_l11, L_l12, L_l13, L_l14, L_l15 = primes[
                                                                                                 num + 735:num + 750]
M_l1, M_l2, M_l3, M_l4, M_l5, M_l6, M_l7, M_l8, M_l9, M_l10, M_l11, M_l12, M_l13, M_l14, M_l15 = primes[
                                                                                                 num + 750:num + 765]
N_l1, N_l2, N_l3, N_l4, N_l5, N_l6, N_l7, N_l8, N_l9, N_l10, N_l11, N_l12, N_l13, N_l14, N_l15 = primes[
                                                                                                 num + 765:num + 780]
O_l1, O_l2, O_l3, O_l4, O_l5, O_l6, O_l7, O_l8, O_l9, O_l10, O_l11, O_l12, O_l13, O_l14, O_l15 = primes[
                                                                                                 num + 780:num + 795]
P_l1, P_l2, P_l3, P_l4, P_l5, P_l6, P_l7, P_l8, P_l9, P_l10, P_l11, P_l12, P_l13, P_l14, P_l15 = primes[
                                                                                                 num + 795:num + 810]
Q_l1, Q_l2, Q_l3, Q_l4, Q_l5, Q_l6, Q_l7, Q_l8, Q_l9, Q_l10, Q_l11, Q_l12, Q_l13, Q_l14, Q_l15 = primes[
                                                                                                 num + 810:num + 825]
R_l1, R_l2, R_l3, R_l4, R_l5, R_l6, R_l7, R_l8, R_l9, R_l10, R_l11, R_l12, R_l13, R_l14, R_l15 = primes[
                                                                                                 num + 825:num + 840]
S_l1, S_l2, S_l3, S_l4, S_l5, S_l6, S_l7, S_l8, S_l9, S_l10, S_l11, S_l12, S_l13, S_l14, S_l15 = primes[
                                                                                                 num + 840:num + 855]
T_l1, T_l2, T_l3, T_l4, T_l5, T_l6, T_l7, T_l8, T_l9, T_l10, T_l11, T_l12, T_l13, T_l14, T_l15 = primes[
                                                                                                 num + 855:num + 870]
U_l1, U_l2, U_l3, U_l4, U_l5, U_l6, U_l7, U_l8, U_l9, U_l10, U_l11, U_l12, U_l13, U_l14, U_l15 = primes[
                                                                                                 num + 870:num + 885]
V_l1, V_l2, V_l3, V_l4, V_l5, V_l6, V_l7, V_l8, V_l9, V_l10, V_l11, V_l12, V_l13, V_l14, V_l15 = primes[
                                                                                                 num + 885:num + 900]
W_l1, W_l2, W_l3, W_l4, W_l5, W_l6, W_l7, W_l8, W_l9, W_l10, W_l11, W_l12, W_l13, W_l14, W_l15 = primes[
                                                                                                 num + 900:num + 915]
X_l1, X_l2, X_l3, X_l4, X_l5, X_l6, X_l7, X_l8, X_l9, X_l10, X_l11, X_l12, X_l13, X_l14, X_l15 = primes[
                                                                                                 num + 915:num + 930]
Y_l1, Y_l2, Y_l3, Y_l4, Y_l5, Y_l6, Y_l7, Y_l8, Y_l9, Y_l10, Y_l11, Y_l12, Y_l13, Y_l14, Y_l15 = primes[
                                                                                                 num + 930:num + 945]
Z_l1, Z_l2, Z_l3, Z_l4, Z_l5, Z_l6, Z_l7, Z_l8, Z_l9, Z_l10, Z_l11, Z_l12, Z_l13, Z_l14, Z_l15 = primes[
                                                                                                 num + 945:num + 960]

def user_sign_in(password, Email):

    try:
        with open(rf"{path}/{Email}/random_number.txt", 'r') as f:
            random_number = f.read()
        num = int(random_number)

    ################################################################################################

        a_l1, a_l2, a_l3, a_l4, a_l5, a_l6, a_l7, a_l8, a_l9, a_l10, a_l11, a_l12, a_l13, a_l14, a_l15 = primes[
                                                                                                         num:num + 15]
        b_l1, b_l2, b_l3, b_l4, b_l5, b_l6, b_l7, b_l8, b_l9, b_l10, b_l11, b_l12, b_l13, b_l14, b_l15 = primes[
                                                                                                         num + 15:num + 30]
        c_l1, c_l2, c_l3, c_l4, c_l5, c_l6, c_l7, c_l8, c_l9, c_l10, c_l11, c_l12, c_l13, c_l14, c_l15 = primes[
                                                                                                         num + 30:num + 45]
        d_l1, d_l2, d_l3, d_l4, d_l5, d_l6, d_l7, d_l8, d_l9, d_l10, d_l11, d_l12, d_l13, d_l14, d_l15 = primes[
                                                                                                         num + 45:num + 60]
        e_l1, e_l2, e_l3, e_l4, e_l5, e_l6, e_l7, e_l8, e_l9, e_l10, e_l11, e_l12, e_l13, e_l14, e_l15 = primes[
                                                                                                         num + 60:num + 75]
        f_l1, f_l2, f_l3, f_l4, f_l5, f_l6, f_l7, f_l8, f_l9, f_l10, f_l11, f_l12, f_l13, f_l14, f_l15 = primes[
                                                                                                         num + 75:num + 90]
        g_l1, g_l2, g_l3, g_l4, g_l5, g_l6, g_l7, g_l8, g_l9, g_l10, g_l11, g_l12, g_l13, g_l14, g_l15 = primes[
                                                                                                         num + 90:num + 105]
        h_l1, h_l2, h_l3, h_l4, h_l5, h_l6, h_l7, h_l8, h_l9, h_l10, h_l11, h_l12, h_l13, h_l14, h_l15 = primes[
                                                                                                         num + 105:num + 120]
        i_l1, i_l2, i_l3, i_l4, i_l5, i_l6, i_l7, i_l8, i_l9, i_l10, i_l11, i_l12, i_l13, i_l14, i_l15 = primes[
                                                                                                         num + 120:num + 135]
        j_l1, j_l2, j_l3, j_l4, j_l5, j_l6, j_l7, j_l8, j_l9, j_l10, j_l11, j_l12, j_l13, j_l14, j_l15 = primes[
                                                                                                         num + 135:num + 150]
        k_l1, k_l2, k_l3, k_l4, k_l5, k_l6, k_l7, k_l8, k_l9, k_l10, k_l11, k_l12, k_l13, k_l14, k_l15 = primes[
                                                                                                         num + 150:num + 165]
        l_l1, l_l2, l_l3, l_l4, l_l5, l_l6, l_l7, l_l8, l_l9, l_l10, l_l11, l_l12, l_l13, l_l14, l_l15 = primes[
                                                                                                         num + 165:num + 180]
        m_l1, m_l2, m_l3, m_l4, m_l5, m_l6, m_l7, m_l8, m_l9, m_l10, m_l11, m_l12, m_l13, m_l14, m_l15 = primes[
                                                                                                         num + 180:num + 195]
        n_l1, n_l2, n_l3, n_l4, n_l5, n_l6, n_l7, n_l8, n_l9, n_l10, n_l11, n_l12, n_l13, n_l14, n_l15 = primes[
                                                                                                         num + 195:num + 210]
        o_l1, o_l2, o_l3, o_l4, o_l5, o_l6, o_l7, o_l8, o_l9, o_l10, o_l11, o_l12, o_l13, o_l14, o_l15 = primes[
                                                                                                         num + 210:num + 225]
        p_l1, p_l2, p_l3, p_l4, p_l5, p_l6, p_l7, p_l8, p_l9, p_l10, p_l11, p_l12, p_l13, p_l14, p_l15 = primes[
                                                                                                         num + 225:num + 240]
        q_l1, q_l2, q_l3, q_l4, q_l5, q_l6, q_l7, q_l8, q_l9, q_l10, q_l11, q_l12, q_l13, q_l14, q_l15 = primes[
                                                                                                         num + 240:num + 255]
        r_l1, r_l2, r_l3, r_l4, r_l5, r_l6, r_l7, r_l8, r_l9, r_l10, r_l11, r_l12, r_l13, r_l14, r_l15 = primes[
                                                                                                         num + 255:num + 270]
        s_l1, s_l2, s_l3, s_l4, s_l5, s_l6, s_l7, s_l8, s_l9, s_l10, s_l11, s_l12, s_l13, s_l14, s_l15 = primes[
                                                                                                         num + 270:num + 285]
        t_l1, t_l2, t_l3, t_l4, t_l5, t_l6, t_l7, t_l8, t_l9, t_l10, t_l11, t_l12, t_l13, t_l14, t_l15 = primes[
                                                                                                         num + 285:num + 300]
        u_l1, u_l2, u_l3, u_l4, u_l5, u_l6, u_l7, u_l8, u_l9, u_l10, u_l11, u_l12, u_l13, u_l14, u_l15 = primes[
                                                                                                         num + 300:num + 315]
        v_l1, v_l2, v_l3, v_l4, v_l5, v_l6, v_l7, v_l8, v_l9, v_l10, v_l11, v_l12, v_l13, v_l14, v_l15 = primes[
                                                                                                         num + 315:num + 330]
        w_l1, w_l2, w_l3, w_l4, w_l5, w_l6, w_l7, w_l8, w_l9, w_l10, w_l11, w_l12, w_l13, w_l14, w_l15 = primes[
                                                                                                         num + 330:num + 345]
        x_l1, x_l2, x_l3, x_l4, x_l5, x_l6, x_l7, x_l8, x_l9, x_l10, x_l11, x_l12, x_l13, x_l14, x_l15 = primes[
                                                                                                         num + 345:num + 360]
        y_l1, y_l2, y_l3, y_l4, y_l5, y_l6, y_l7, y_l8, y_l9, y_l10, y_l11, y_l12, y_l13, y_l14, y_l15 = primes[
                                                                                                         num + 360:num + 375]
        z_l1, z_l2, z_l3, z_l4, z_l5, z_l6, z_l7, z_l8, z_l9, z_l10, z_l11, z_l12, z_l13, z_l14, z_l15 = primes[
                                                                                                         num + 375:num + 390]
        l_0_1, l_0_2, l_0_3, l_0_4, l_0_5, l_0_6, l_0_7, l_0_8, l_0_9, l_0_10, l_0_11, l_0_12, l_0_13, l_0_14, l_0_15 = primes[
                                                                                                                        num + 405:num + 420]
        l_1_1, l_1_2, l_1_3, l_1_4, l_1_5, l_1_6, l_1_7, l_1_8, l_1_9, l_1_10, l_1_11, l_1_12, l_1_13, l_1_14, l_1_15 = primes[
                                                                                                                        num + 420:num + 435]
        l_2_1, l_2_2, l_2_3, l_2_4, l_2_5, l_2_6, l_2_7, l_2_8, l_2_9, l_2_10, l_2_11, l_2_12, l_2_13, l_2_14, l_2_15 = primes[
                                                                                                                        num + 435:num + 450]
        l_3_1, l_3_2, l_3_3, l_3_4, l_3_5, l_3_6, l_3_7, l_3_8, l_3_9, l_3_10, l_3_11, l_3_12, l_3_13, l_3_14, l_3_15 = primes[
                                                                                                                        num + 450:num + 465]
        l_4_1, l_4_2, l_4_3, l_4_4, l_4_5, l_4_6, l_4_7, l_4_8, l_4_9, l_4_10, l_4_11, l_4_12, l_4_13, l_4_14, l_4_15 = primes[
                                                                                                                        num + 465:num + 480]
        l_5_1, l_5_2, l_5_3, l_5_4, l_5_5, l_5_6, l_5_7, l_5_8, l_5_9, l_5_10, l_5_11, l_5_12, l_5_13, l_5_14, l_5_15 = primes[
                                                                                                                        num + 480:num + 495]
        l_6_1, l_6_2, l_6_3, l_6_4, l_6_5, l_6_6, l_6_7, l_6_8, l_6_9, l_6_10, l_6_11, l_6_12, l_6_13, l_6_14, l_6_15 = primes[
                                                                                                                        num + 495:num + 510]
        l_7_1, l_7_2, l_7_3, l_7_4, l_7_5, l_7_6, l_7_7, l_7_8, l_7_9, l_7_10, l_7_11, l_7_12, l_7_13, l_7_14, l_7_15 = primes[
                                                                                                                        num + 510:num + 525]
        l_8_1, l_8_2, l_8_3, l_8_4, l_8_5, l_8_6, l_8_7, l_8_8, l_8_9, l_8_10, l_8_11, l_8_12, l_8_13, l_8_14, l_8_15 = primes[
                                                                                                                        num + 525:num + 540]
        l_9_1, l_9_2, l_9_3, l_9_4, l_9_5, l_9_6, l_9_7, l_9_8, l_9_9, l_9_10, l_9_11, l_9_12, l_9_13, l_9_14, l_9_15 = primes[
                                                                                                                        num + 540:num + 555]

        A_l1, A_l2, A_l3, A_l4, A_l5, A_l6, A_l7, A_l8, A_l9, A_l10, A_l11, A_l12, A_l13, A_l14, A_l15 = primes[
                                                                                                         num + 570:num + 585]
        B_l1, B_l2, B_l3, B_l4, B_l5, B_l6, B_l7, B_l8, B_l9, B_l10, B_l11, B_l12, B_l13, B_l14, B_l15 = primes[
                                                                                                         num + 585:num + 600]
        C_l1, C_l2, C_l3, C_l4, C_l5, C_l6, C_l7, C_l8, C_l9, C_l10, C_l11, C_l12, C_l13, C_l14, C_l15 = primes[
                                                                                                         num + 600:num + 615]
        D_l1, D_l2, D_l3, D_l4, D_l5, D_l6, D_l7, D_l8, D_l9, D_l10, D_l11, D_l12, D_l13, D_l14, D_l15 = primes[
                                                                                                         num + 615:num + 630]
        E_l1, E_l2, E_l3, E_l4, E_l5, E_l6, E_l7, E_l8, E_l9, E_l10, E_l11, E_l12, E_l13, E_l14, E_l15 = primes[
                                                                                                         num + 630:num + 645]
        F_l1, F_l2, F_l3, F_l4, F_l5, F_l6, F_l7, F_l8, F_l9, F_l10, F_l11, F_l12, F_l13, F_l14, F_l15 = primes[
                                                                                                         num + 645:num + 660]
        G_l1, G_l2, G_l3, G_l4, G_l5, G_l6, G_l7, G_l8, G_l9, G_l10, G_l11, G_l12, G_l13, G_l14, G_l15 = primes[
                                                                                                         num + 660:num + 675]
        H_l1, H_l2, H_l3, H_l4, H_l5, H_l6, H_l7, H_l8, H_l9, H_l10, H_l11, H_l12, H_l13, H_l14, H_l15 = primes[
                                                                                                         num + 675:num + 690]
        I_l1, I_l2, I_l3, I_l4, I_l5, I_l6, I_l7, I_l8, I_l9, I_l10, I_l11, I_l12, I_l13, I_l14, I_l15 = primes[
                                                                                                         num + 690:num + 705]
        J_l1, J_l2, J_l3, J_l4, J_l5, J_l6, J_l7, J_l8, J_l9, J_l10, J_l11, J_l12, J_l13, J_l14, J_l15 = primes[
                                                                                                         num + 705:num + 720]
        K_l1, K_l2, K_l3, K_l4, K_l5, K_l6, K_l7, K_l8, K_l9, K_l10, K_l11, K_l12, K_l13, K_l14, K_l15 = primes[
                                                                                                         num + 720:num + 735]
        L_l1, L_l2, L_l3, L_l4, L_l5, L_l6, L_l7, L_l8, L_l9, L_l10, L_l11, L_l12, L_l13, L_l14, L_l15 = primes[
                                                                                                         num + 735:num + 750]
        M_l1, M_l2, M_l3, M_l4, M_l5, M_l6, M_l7, M_l8, M_l9, M_l10, M_l11, M_l12, M_l13, M_l14, M_l15 = primes[
                                                                                                         num + 750:num + 765]
        N_l1, N_l2, N_l3, N_l4, N_l5, N_l6, N_l7, N_l8, N_l9, N_l10, N_l11, N_l12, N_l13, N_l14, N_l15 = primes[
                                                                                                         num + 765:num + 780]
        O_l1, O_l2, O_l3, O_l4, O_l5, O_l6, O_l7, O_l8, O_l9, O_l10, O_l11, O_l12, O_l13, O_l14, O_l15 = primes[
                                                                                                         num + 780:num + 795]
        P_l1, P_l2, P_l3, P_l4, P_l5, P_l6, P_l7, P_l8, P_l9, P_l10, P_l11, P_l12, P_l13, P_l14, P_l15 = primes[
                                                                                                         num + 795:num + 810]
        Q_l1, Q_l2, Q_l3, Q_l4, Q_l5, Q_l6, Q_l7, Q_l8, Q_l9, Q_l10, Q_l11, Q_l12, Q_l13, Q_l14, Q_l15 = primes[
                                                                                                         num + 810:num + 825]
        R_l1, R_l2, R_l3, R_l4, R_l5, R_l6, R_l7, R_l8, R_l9, R_l10, R_l11, R_l12, R_l13, R_l14, R_l15 = primes[
                                                                                                         num + 825:num + 840]
        S_l1, S_l2, S_l3, S_l4, S_l5, S_l6, S_l7, S_l8, S_l9, S_l10, S_l11, S_l12, S_l13, S_l14, S_l15 = primes[
                                                                                                         num + 840:num + 855]
        T_l1, T_l2, T_l3, T_l4, T_l5, T_l6, T_l7, T_l8, T_l9, T_l10, T_l11, T_l12, T_l13, T_l14, T_l15 = primes[
                                                                                                         num + 855:num + 870]
        U_l1, U_l2, U_l3, U_l4, U_l5, U_l6, U_l7, U_l8, U_l9, U_l10, U_l11, U_l12, U_l13, U_l14, U_l15 = primes[
                                                                                                         num + 870:num + 885]
        V_l1, V_l2, V_l3, V_l4, V_l5, V_l6, V_l7, V_l8, V_l9, V_l10, V_l11, V_l12, V_l13, V_l14, V_l15 = primes[
                                                                                                         num + 885:num + 900]
        W_l1, W_l2, W_l3, W_l4, W_l5, W_l6, W_l7, W_l8, W_l9, W_l10, W_l11, W_l12, W_l13, W_l14, W_l15 = primes[
                                                                                                         num + 900:num + 915]
        X_l1, X_l2, X_l3, X_l4, X_l5, X_l6, X_l7, X_l8, X_l9, X_l10, X_l11, X_l12, X_l13, X_l14, X_l15 = primes[
                                                                                                         num + 915:num + 930]
        Y_l1, Y_l2, Y_l3, Y_l4, Y_l5, Y_l6, Y_l7, Y_l8, Y_l9, Y_l10, Y_l11, Y_l12, Y_l13, Y_l14, Y_l15 = primes[
                                                                                                         num + 930:num + 945]
        Z_l1, Z_l2, Z_l3, Z_l4, Z_l5, Z_l6, Z_l7, Z_l8, Z_l9, Z_l10, Z_l11, Z_l12, Z_l13, Z_l14, Z_l15 = primes[
                                                                                                         num + 945:num + 960]

    ###################################################################################################
    except:
        pass



    try:
        with open(rf"{path}/{Email}/password.txt", 'r') as f:
            data_kb = f.read()

        user_enter_password = password
        user_input_list = list(user_enter_password)
        user_input_string_or_number = 1
        total_prime_product = 1
        for x in user_input_list:
            if x not in "1234567890":
                s = f"{x}_l{user_input_string_or_number}"
                sint = int(eval(s))
                total_prime_product *= sint
                user_input_string_or_number += 1
            else:
                s = f"l_{x}_{user_input_string_or_number}"
                sint = int(eval(s))
                total_prime_product *= sint
                user_input_string_or_number += 1
        if argon2.verify(str(total_prime_product), data_kb):
            return True
        else:
            return False
    except:
        return False

def savePassword(password, email, name):
    try:
        createFolder(rf"{path}/{email}")
        createFolder(rf"{path}/{email}/file_saver")
        createFolder(rf"{path}/{email}/short_cuts")
        createFolder(rf"{path}/{email}/short_cuts_words")
        createFolder(rf"{path}/{email}/schedule")
        with open(rf"{path}/{email}/Direction.txt", 'w') as f:
            f.write(Common.getlanguagesForFile())
        f.close()
        with open(rf"{path}/{email}/OpenWindow.txt", 'w') as f:
            f.write("True")
        f.close()
        with open(rf"{path}/{email}/CloseWindow.txt", 'w') as f:
            f.write("False")
        f.close()
        with open(rf"{path}\{email}\schedule\['2020', '1', '1'] & ['00', '00', '00'] & system_file", 'w') as f:
            f.write("This file is used by the software. Do not change it.")
        f.close()
        with open(rf"{path}\{email}\first_log_in.txt", 'w') as f:
            f.write("yes")
        f.close()

    except:
        return False


    with open(rf"{path}/{email}/random_number.txt", 'w') as f:
        f.write(str(num))
    f.close()

    user_input = password
    user_input_list = list(user_input)
    user_input_string_or_number = 1
    total_prime_product = 1
    for x in user_input_list:
        if x not in "1234567890":
            s = f"{x}_l{user_input_string_or_number}"
            sint = int(eval(s))
            total_prime_product *= sint
            user_input_string_or_number += 1
        else:
            s = f"l_{x}_{user_input_string_or_number}"
            sint = int(eval(s))
            total_prime_product *= sint
            user_input_string_or_number += 1

    hash_password = argon2.hash(str(total_prime_product))

    with open(rf"{path}/{email}/password.txt", 'w') as f1:
        f1.write(str(hash_password))
        f1.close()
    with open(rf"{path}/{email}/name.txt", 'w') as nameFile:
        nameFile.write(name)
        nameFile.close()


def savePasswordForgotPassoword(password, email):
    with open(rf"{path}/{email}/random_number.txt", 'w') as f:
        f.write(str(num))
        f.close()
    user_input = password
    user_input_list = list(user_input)
    user_input_string_or_number = 1
    total_prime_product = 1
    for x in user_input_list:
        if x not in "1234567890":
            s = f"{x}_l{user_input_string_or_number}"
            sint = int(eval(s))
            total_prime_product *= sint
            user_input_string_or_number += 1
        else:
            s = f"l_{x}_{user_input_string_or_number}"
            sint = int(eval(s))
            total_prime_product *= sint
            user_input_string_or_number += 1
    hash_password = argon2.hash(str(total_prime_product))
    with open(rf"{path}/{email}/password.txt", 'w') as f1:
        f1.write(str(hash_password))
        f1.close()