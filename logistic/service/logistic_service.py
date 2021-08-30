import json
from django.db import IntegrityError

import logistic.service.logistic_service
from logistic.models import City,Logistics,Zone,Rate
from logistic.data.response.logistics import Logistics_Response
from grihasoft.message import Message,SuccessMessage,SuccessStatus,ErrorMessage
from logistic.util.logistic_util import City_Part

class Logistics_Service:
    def insert_logistics(self ,request_obj,obj,userid):
        if 'id' in obj:
            try:
                user = Logistics.objects.filter(id=request_obj.get_id()).update(fromcity_id=obj['source'],
                                                                    tocity_id = obj['destination'],
                                                                    zone = obj['zone'],
                                                                    rate = obj['rate'],
                                                                    weight = obj['weight'],
                                                                    updated_by = userid)
            except Exception as e:
                print(e)
                print(e)
                msg_obj = Message()
                msg_obj.set_status(SuccessStatus.ERROR)
                msg_obj.set_message(e)
                return msg_obj

            msg_obj = Message()
            msg_obj.set_status(SuccessStatus.SUCCESS)
            msg_obj.set_message({"userid":user.id})
            return msg_obj

        else:
            try:
                user = Logistics.objects.create(
                    fromcity_id=obj['source'],
                    tocity_id=obj['destination'],
                    zone=obj['zone'],
                    rate=obj['rate'],
                    weight=obj['weight'],
                    create_by=userid,
                    status = 1)
            except Exception as e:
                print(e)
                msg_obj = Message()
                msg_obj.set_status(SuccessStatus.ERROR)
                msg_obj.set_message(e)
                return msg_obj


            msg_obj = Message()
            msg_obj.set_status(SuccessStatus.SUCCESS)
            msg_obj.set_message({"userid":user.id})
            return msg_obj

    def get_rate_logistics(self,data):
        try:
            zone = Zone.objects.get(source=data.get_source(),destination=data.get_destination())
            rate = Rate.objects.get(weight=data.get_weight(), zone=zone.zone)
            req_data = Logistics_Response()
            req_data.set_zone(zone.zone)
            req_data.set_rate(rate.rate)
            msg_obj = Message()
            msg_obj.set_status(SuccessStatus.SUCCESS)
            msg_obj.set_message(json.loads(req_data.get()))
            return msg_obj

        except Exception as e:
            print(e)
            msg_obj = Message()
            msg_obj.set_status(SuccessStatus.ERROR)
            msg_obj.set_message(ErrorMessage.DATAMISSING)
            return msg_obj

    def insert_city(self ,request_obj,obj,userid):
        if 'id' in obj:
            try:
                part = City_Part.get_id(self, obj['part'])
                city = City.objects.filter(id=obj['id']).update(name=obj['name'],
                                                                    part = part,
                                                                    updated_by = userid)
            except Exception as e:
                print(e)
                print(e)
                msg_obj = Message()
                msg_obj.set_status(SuccessStatus.ERROR)
                msg_obj.set_message(e)
                return msg_obj

            msg_obj = Message()
            msg_obj.set_status(SuccessStatus.SUCCESS)
            msg_obj.set_message({"cityid":city})
            return msg_obj

        else:
            try:
                part = City_Part.get_id(self,obj['part'])
                city = City.objects.create(
                    name=obj['name'],
                    part = part,
                    create_by = userid,
                    status = 1)
            except Exception as e:
                print(e)
                msg_obj = Message()
                msg_obj.set_status(SuccessStatus.ERROR)
                msg_obj.set_message(e)
                return msg_obj


            msg_obj = Message()
            msg_obj.set_status(SuccessStatus.SUCCESS)
            msg_obj.set_message({"cityid":city.id})
            return msg_obj

    def insert_zone(self ,request_obj,obj,userid):
        if 'id' in obj:
            try:
                zone = Zone.objects.filter(id=obj['id']).update(source=obj['source'],
                                                                    destination = obj['destination'],
                                                                    zone = obj['zone'],
                                                                    updated_by = userid)
            except Exception as e:
                print(e)
                print(e)
                msg_obj = Message()
                msg_obj.set_status(SuccessStatus.ERROR)
                msg_obj.set_message(e)
                return msg_obj

            msg_obj = Message()
            msg_obj.set_status(SuccessStatus.SUCCESS)
            msg_obj.set_message({"zoneid":zone})
            return msg_obj

        else:
            try:
                zone = Zone.objects.create(
                    source=obj['source'],
                    destination = obj['destination'],
                    zone = obj['zone'],
                    create_by=userid,
                    status = 1)
            except Exception as e:
                print(e)
                msg_obj = Message()
                msg_obj.set_status(SuccessStatus.ERROR)
                msg_obj.set_message(e)
                return msg_obj


            msg_obj = Message()
            msg_obj.set_status(SuccessStatus.SUCCESS)
            msg_obj.set_message({"zoneid":zone.id})
            return msg_obj

    def insert_rate(self ,request_obj,obj,userid):
        if 'id' in obj:
            try:
                rate = Rate.objects.filter(id=obj['id']).update(weight=obj['weight'],
                                                                    zone = obj['zone'],
                                                                    rate = obj['rate'],
                                                                    updated_by = userid)
            except Exception as e:
                print(e)
                print(e)
                msg_obj = Message()
                msg_obj.set_status(SuccessStatus.ERROR)
                msg_obj.set_message(e)
                return msg_obj

            msg_obj = Message()
            msg_obj.set_status(SuccessStatus.SUCCESS)
            msg_obj.set_message({"rateid":rate})
            return msg_obj

        else:
            try:
                rate = Rate.objects.create(
                    weight=obj['weight'],
                    rate = obj['rate'],
                    zone = obj['zone'],
                    create_by=userid,
                    status = 1)
            except Exception as e:
                print(e)
                msg_obj = Message()
                msg_obj.set_status(SuccessStatus.ERROR)
                msg_obj.set_message(e)
                return msg_obj


            msg_obj = Message()
            msg_obj.set_status(SuccessStatus.SUCCESS)
            msg_obj.set_message({"rateid":rate.id})
            return msg_obj

    def get_cityid(self,id):
        city = City.objects.get(id=id)
        return city.name

    def get_city(self):
        city = City.objects.all()
        resp_list = Logistics_Response()
        ar =[]
        for i in city:
            req_data = Logistics_Response()
            req_data.set_id(i.id)
            req_data.set_city(i.name)
            req_data.set_partname(City_Part.get_part(self, int(i.part)))
            req_data.set_part(i.part)
            req_data.set_status(i.status)
            ar.append(json.loads(req_data.get()))
        resp_list.set_data(ar)
        return resp_list

    def get_zone(self):
        zone = Zone.objects.all()
        resp_list = Logistics_Response()
        ar =[]
        for i in zone:
            req_data = Logistics_Response()
            req_data.set_id(i.id)
            req_data.set_source(i.source)
            req_data.set_sourcename(City_Part.get_part(self, i.source))
            req_data.set_destination(i.destination)
            req_data.set_destinationname(City_Part.get_part(self,i.destination))
            req_data.set_zone(i.zone)
            req_data.set_status(i.status)
            ar.append(json.loads(req_data.get()))
        resp_list.set_data(ar)
        return resp_list

    def get_rate(self):
        rate = Rate.objects.all()
        resp_list = Logistics_Response()
        ar =[]
        for i in rate:
            req_data = Logistics_Response()
            req_data.set_id(i.id)
            req_data.set_weight(i.weight)
            req_data.set_rate(i.rate)
            req_data.set_zone(i.zone)
            req_data.set_status(i.status)
            ar.append(json.loads(req_data.get()))
        resp_list.set_data(ar)
        return resp_list

    def get_logistics(self):
        logistics = Logistics.objects.all()
        resp_list = Logistics_Response()
        ar =[]
        for i in logistics:
            req_data = Logistics_Response()
            req_data.set_id(i.id)
            req_data.set_weight(i.weight)
            req_data.set_source(i.fromcity_id)
            req_data.set_sourcename(logistic.service.logistic_service.Logistics_Service.get_cityid(self,i.fromcity_id))
            req_data.set_destination(i.tocity_id)
            req_data.set_destinationname(logistic.service.logistic_service.Logistics_Service.get_cityid(self,i.tocity_id))
            req_data.set_rate(i.rate)
            req_data.set_zone(i.zone)
            req_data.set_status(i.status)
            ar.append(json.loads(req_data.get()))
        resp_list.set_data(ar)
        return resp_list

