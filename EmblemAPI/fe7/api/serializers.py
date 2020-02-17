from rest_framework import serializers
from fe7.models import Character, BaseStats, GrowthRates

class BaseStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseStats
        fields = [
            'level', 'hp', 'strength', 'magic', 'skill',
            'speed', 'luck', 'defence', 'resistance',
            'constitution', 'move'
        ]

class GrowthRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrowthRates
        fields = [
            'hp', 'strength', 'magic', 'skill',
            'speed', 'luck', 'defence', 'resistance'
        ]


class CharacterSerializer(serializers.ModelSerializer):
    base_stats = BaseStatSerializer()
    growth_rates = GrowthRateSerializer()

    class Meta:
        model = Character
        fields = [
            'pk', 'name', 'description', 'base_class', 'recruitment_chapter',
            'strength_user', 'magic_user', 'affinity', 'base_stats',
            'growth_rates',
        ]

    def create(self, validated_data):
        base_stat_data = validated_data.pop('base_stats')
        growth_rate_data = validated_data.pop('growth_rates')
        character = Character.objects.create(**validated_data)
        BaseStats.objects.create(character=character, **base_stat_data)
        GrowthRates.objects.create(character=character, **growth_rate_data)
        return character

    def update(self, instance, validated_data):
        base_stat_data = validated_data.pop('base_stats')
        growth_rate_data = validated_data.pop('growth_rates')
        character = Character.objects.update(**validated_data)
        BaseStats.objects.update(character=character, **base_stat_data)
        GrowthRates.objects.update(character=character, **growth_rate_data)
        return character
