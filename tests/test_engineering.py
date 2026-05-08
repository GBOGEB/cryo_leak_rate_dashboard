from src.calculations.engineering import leak_rate_to_mass_flow_g_s, SECONDS_PER_YEAR


def test_reference_conversion_order_of_magnitude():
    g_s = leak_rate_to_mass_flow_g_s(1e-8, 300, 1)
    g_year = g_s * SECONDS_PER_YEAR
    # Reference requirement table indicates approximately 0.050 g/year for 1e-8 class.
    assert 0.045 <= g_year <= 0.055
