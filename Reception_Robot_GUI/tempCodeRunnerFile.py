        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 8))
        plt.imshow(self.cost_map, cmap='hot')
        plt.colorbar(label='Chi phí')
        plt.title('Cost Map')
        plt.show()