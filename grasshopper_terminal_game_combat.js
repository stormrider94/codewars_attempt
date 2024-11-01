function combat(health, damage) {
    new_health = damage < health ? health-damage : 0
    return new_health
  }