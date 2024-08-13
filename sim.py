import numpy as np
import matplotlib.pyplot as plt
import sys

# Constants
HEIGHT_NET = 2.35  # meters
BALL_DIAMETER = 0.21  # meters
BALL_RADIUS = BALL_DIAMETER * 0.5


def calc_ball_ground_contact_net_distance(x_dist, y_dist):
    """
    Calculates the distance from where the ball is hitting the ground to the net.
    Formula is derived from the 'theorem of intersecting lines' (german: "Strahlensatz")
    """
    try:
        net_distance_x = (x_dist + BALL_RADIUS) / ((y_dist / (HEIGHT_NET + BALL_RADIUS)) - 1)
        return net_distance_x

    except ZeroDivisionError:
        print("Boundaries lead to division by zero. Please adjust boundaries")
        sys.exit()


if __name__ == "__main__":
    # Setting boundaries for graph
    spike_x_distance_lower = 0  # meters
    spike_x_distance_upper = 3  # meters

    spike_y_distance_lower = 2.5  # Must be greater than HEIGHT_NET, in meters
    spike_y_distance_upper = 4  # meters

    # Generate grid based on boundaries
    x = np.linspace(spike_x_distance_lower, spike_x_distance_upper, 100)
    y = np.linspace(spike_y_distance_lower, spike_y_distance_upper, 100)

    X, Y = np.meshgrid(x, y)

    # Compute the corresponding z values (x_distance where the ball will hit the ground on the other side of the net)
    Z = calc_ball_ground_contact_net_distance(X, Y)

    # Add contour lines for topography
    contour_levels = np.linspace(0, 9, 10)
    contour = plt.contour(X, Y, Z, levels=contour_levels, colors='black')
    plt.clabel(contour, inline=1, fontsize=10, fmt='%0.1f')

    # Add a fine grid with tick labels only at every other gridline
    x_grid_spacing = 0.2
    y_grid_spacing = 0.1

    plt.grid(True, linestyle='--', alpha=0.4, which='both')  # Show both major and minor gridlines
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(x_grid_spacing))  # Set major tick spacing
    plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(x_grid_spacing / 2))  # Set minor tick spacing

    plt.yticks(np.arange(y.min(), y.max(), y_grid_spacing))  # Adjust the y-grid spacing as needed

    # Add labels and a title
    plt.title('Ball ground contact distance to net')
    plt.xlabel('Distance to net [m]')
    plt.ylabel('Spike height [m]')

    plt.savefig('spike_sim.png', format='png', dpi=300)
    # plt.savefig('spike_sim.svg', format='svg')

    # Show the plot
    # plt.show()
