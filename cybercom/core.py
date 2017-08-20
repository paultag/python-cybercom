import cryptography.x509
from cryptography.hazmat.backends import default_backend

import cybercom.pb
import grpc


class Client(object):
    def __init__(self, server, creds, *args, **kwargs):
        self.channel = grpc.secure_channel(server, creds)
        self.stub = cybercom.pb.CybercomStub(self.channel)

    def get_configuration(self):
        return Configuration.from_pb(self.stub.GetConfiguration(cybercom.pb.Empty()))

    def get_entities(self):
        for entity in self.stub.GetEntities(cybercom.pb.Empty()):
            yield Entity.from_pb(entity)

    def get_entity(self, id):
        return Entity.from_pb(self.stub.GetEntity(cybercom.pb.Id(id=id)))

    def get_certificates(self, id):
        for cert in self.stub.GetCertificates(cybercom.pb.Id(id=id)):
            yield cryptography.x509.load_der_x509_certificate(cert.der, default_backend())

    def get_certificate(self, id):
        cert = self.stub.GetCertificate(cybercom.pb.Id(id=id))
        return cryptography.x509.load_der_x509_certificate(cert.der, default_backend())

    def get_certificate_by_serial(self, id):
        cert = self.stub.GetCertificateBySerial(cybercom.pb.Serial(serial=id))
        return cryptography.x509.load_der_x509_certificate(cert.der, default_backend())


class Entity(object):
    def __init__(self, id, state, csr, email, longevity, expires):
        self.id = id
        self.state = state
        self.csr = csr
        self.email = email
        self.longevity = longevity
        self.expires = expires

    def is_pending(self):
        return self.state == cybercom.pb.Entity.PENDING

    def is_inactive(self):
        return self.state in {
            cybercom.pb.Entity.REVOKED,
            cybercom.pb.Entity.REJECTED,
        }

    def is_active(self):
        return self.state in {
            cybercom.pb.Entity.APPROVED,
            cybercom.pb.Entity.ONEOFF,
        }

    @classmethod
    def from_pb(cls, pb):
        csr = cryptography.x509.load_der_x509_csr(pb.csr.der, default_backend())
        return Entity(id=pb.id.id, state=pb.state, csr=csr, email=pb.email,
                      longevity=pb.longevity, expires=pb.expires)

    def __repr__(self):
        return "<Entity: email={}>".format(self.email)


class RequestTemplate(object):
    def __init__(self, country, organization, organizational_unit, locality, province):
        self.country = country
        self.organization = organization
        self.organizational_unit = organizational_unit
        self.locality = locality
        self.province = province

    @classmethod
    def from_pb(cls, pb):
        return RequestTemplate(
            country=pb.country,
            organization=pb.organization,
            organizational_unit=pb.organizational_unit,
            locality=pb.locality,
            province=pb.province,
        )


class Configuration(object):
    def __init__(self, name, request_template, ca_certs, peer, entity):
        self.name = name
        self.request_template = request_template
        self.ca_certs = ca_certs
        self.peer = peer
        self.entity = entity

    @classmethod
    def from_pb(cls, pb):
        template = RequestTemplate.from_pb(pb.request_template)
        ca_certs = [cryptography.x509.load_der_x509_certificate(cert.der, default_backend())
                    for cert in pb.ca]
        peer = cryptography.x509.load_der_x509_certificate(pb.peer.der, default_backend())
        entity = Entity.from_pb(pb.entity)
        return Configuration(name=pb.name, request_template=template,
                             peer=peer, ca_certs=ca_certs, entity=entity)
