import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
import imageio

def create_simple_animation():
    """
    Create a simple animated video with moving shapes
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    
    # Create shapes
    circle = plt.Circle((5, 5), 0.5, color='red')
    ax.add_patch(circle)
    
    def animate(frame):
        """Update animation for each frame"""
        # Move circle in a circle pattern
        angle = frame * 0.1
        x = 5 + 3 * np.cos(angle)
        y = 5 + 3 * np.sin(angle)
        
        circle.center = (x, y)
        
        # Change color based on frame
        hue = (frame % 100) / 100
        circle.set_color(plt.cm.hsv(hue))
        
        return circle,
    
    # Create animation
    anim = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
    
    # Save as video
    anim.save('animation_output.gif', writer=PillowWriter(fps=20))
    print("Animation saved as 'animation_output.gif'")
    plt.close()


def create_particle_animation():
    """
    Create an animated particle system
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.set_facecolor('navy')
    
    # Create particles
    n_particles = 50
    particles_x = np.random.uniform(-10, 10, n_particles)
    particles_y = np.random.uniform(-10, 10, n_particles)
    particles_vx = np.random.uniform(-0.5, 0.5, n_particles)
    particles_vy = np.random.uniform(-0.5, 0.5, n_particles)
    
    scatter = ax.scatter(particles_x, particles_y, c='cyan', s=50, alpha=0.7)
    
    def animate(frame):
        """Update particle positions"""
        nonlocal particles_x, particles_y, particles_vx, particles_vy
        
        # Update positions
        particles_x += particles_vx
        particles_y += particles_vy
        
        # Bounce off walls
        particles_x = np.where(np.abs(particles_x) > 10, -particles_x, particles_x)
        particles_y = np.where(np.abs(particles_y) > 10, -particles_y, particles_y)
        
        # Update scatter plot
        scatter.set_offsets(np.c_[particles_x, particles_y])
        
        # Change color
        colors = plt.cm.rainbow(np.linspace(0, 1, n_particles))
        scatter.set_color(colors)
        
        return scatter,
    
    anim = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)
    anim.save('particle_animation.gif', writer=PillowWriter(fps=20))
    print("Particle animation saved as 'particle_animation.gif'")
    plt.close()


def create_wave_animation():
    """
    Create an animated sine wave
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(-2, 2)
    ax.set_facecolor('lightgray')
    
    x = np.linspace(0, 10, 200)
    line, = ax.plot([], [], lw=2, color='blue')
    
    def animate(frame):
        """Update wave animation"""
        y = np.sin(x - frame * 0.1) * np.cos(frame * 0.05)
        line.set_data(x, y)
        return line,
    
    anim = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)
    anim.save('wave_animation.gif', writer=PillowWriter(fps=20))
    print("Wave animation saved as 'wave_animation.gif'")
    plt.close()


if __name__ == "__main__":
    print("Creating animations...")
    create_simple_animation()
    create_particle_animation()
    create_wave_animation()
    print("All animations created successfully!")
