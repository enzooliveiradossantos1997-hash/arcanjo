
# FarmingCenter
# Author: Enzo Oliveira
# Purpose: Agricultural analytics and loss estimation system
# Legal note: Educational and research prototype. No operational liability.

import numpy as np

def estimate_loss(area_hectares, productivity_ton, loss_rate):
    """Estimate agricultural loss in tons."""
    total_production = area_hectares * productivity_ton
    loss = total_production * loss_rate
    return loss

if __name__ == "__main__":
    loss = estimate_loss(120, 3.5, 0.07)
    print(f"Estimated agricultural loss: {loss:.2f} tons")
