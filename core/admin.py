from django.contrib import admin
from .models import Room, Booking, RoomAvailability

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'price')
    search_fields = ('name', 'description')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'start_date', 'end_date', 'confirmed')
    list_filter = ('confirmed', 'start_date')
    search_fields = ('user__username', 'room__name')

@admin.register(RoomAvailability)
class RoomAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('room', 'date', 'is_available')
    list_filter = ('is_available',)
