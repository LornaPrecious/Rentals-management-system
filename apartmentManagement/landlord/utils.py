from .models import ParentProperty, Unit

def property_details(request):  
    items = []
    try:
        properties = ParentProperty.objects.all()
        for property in properties:
            property_units = Unit.objects.filter(parent_property=property)
            
            property_data = {
                'property': {
                    'property_code': property.property_code,
                    'name': property.name,
                    'property_imageURL': property.property_imageURL,
                    'location': property.location, 
                    'property_type': property.property_type,
                    'total_units': property.total_units,
                    'property_size': property.property_size,
                    'building_age': property.building_age,
                    'management_company': property.management_company,
                    'amenities': property.amenities,
                    'utilities': property.utilities,
                    'maintenance_services': property.maintenance_services,
                    'parking': property.parking,
                    'security_features': property.security_features,
                    'average_rent': property.average_rent,
                    'rules_regulations': property.rules_regulations,
                    'accessibility': property.accessibility,
                    'lease_terms': property.lease_terms,
                    'description': property.description,
                },
                'units': [],
            }
            
            for unit in property_units:
                unit_data = {
                    'unit_number': unit.unit_number, 
                    'unit_imageURL': unit.unit_imageURL,
                    'floor_number': unit.floor_number,
                    'bedrooms': unit.bedrooms,
                    'bathrooms': unit.bathrooms,
                    'unit_size': unit.unit_size,
                    'rent_amount': unit.rent_amount,
                    'security_deposit': unit.security_deposit,
                    'availability': unit.availability,
                    'description': unit.description,
                }
                property_data['units'].append(unit_data)
                
            items.append(property_data)
            
    except Exception as e:
        # Handle exceptions appropriately, e.g., log them
        print(f"An error occurred: {str(e)}")
        
    return {'items': items}
