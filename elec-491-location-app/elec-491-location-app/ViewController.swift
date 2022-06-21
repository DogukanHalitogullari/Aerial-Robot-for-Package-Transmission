//
//  ViewController.swift
//  elec-491-location-app
//
//  Created by Doğukan on 22.02.2022.
//

import UIKit
import CoreLocation
import FirebaseDatabase
import FirebaseFirestore

class ViewController: UIViewController {
    
    var location = [String: Any]()
    @IBOutlet weak var infoLabel: UILabel!
    
    @IBOutlet weak var nutritionPack: UIButton!
    
    @IBOutlet weak var firstAidKit: UIButton!
    
    @IBOutlet weak var contentView: UIView!
    private var locationManager:CLLocationManager?
    private var locations:[CLLocation]?
    private var packageType = ""
    let dataBase = Firestore.firestore().collection("location")
    //let db = dataBase.collection("location").document("location") //in current user document //UIDevice.current.name
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        styleObject()
    }
    
    func styleObject () {
        Style.nutritionPackButton(nutritionPack)
        Style.firstAidKitButton(firstAidKit)
        Style.infoLabel(infoLabel)
        view.backgroundColor = .secondarySystemBackground
        contentView.backgroundColor = .secondarySystemBackground
    }
    func getUserLocation() {
        locationManager = CLLocationManager()
        locationManager?.requestAlwaysAuthorization()
        locationManager?.startUpdatingLocation()
        
       /*location = ["latitude": locations?.last?.coordinate.latitude ?? "","longitude": locations?.last?.coordinate.longitude ?? ""]
        let db = dataBase.collection("location").document("location") //in current user document
        db.updateData([
            "currentLocation": FieldValue.arrayUnion([location]) //arrayUnion -> update data method
        ]) { err in
            if let err = err {
                print(err)
            }
        }*/
        
        locationManager?.delegate = self
        }

    @IBAction func nutritionPackButtonTapped(_ sender: Any) {
        let alert = UIAlertController(title: "Alert!!!", message: "Do you want to send NUTRITION package to your current location?", preferredStyle: UIAlertController.Style.alert);
        let yesButton = UIAlertAction(title: "Yes", style: UIAlertAction.Style.default) {
            action in
            self.getUserLocation()
            self.packageType = "nutritionPack"
            self.dataBase.document("location").setData([
                "situation": true,
                "packageType": self.packageType
            ]) { err in
                if let err = err {
                    print("Error writing document: \(err)")
                } else {
                    print("Document successfully written!")
                }
            }
        }
        
        let noButton = UIAlertAction(title: "No", style: UIAlertAction.Style.destructive) {
            action in
        }
        alert.addAction(noButton);
        alert.addAction(yesButton);
        self.present(alert, animated: true, completion: nil)
    }
    
    @IBAction func firstAidKitButtonTapped(_ sender: Any) {
        let alert = UIAlertController(title: "Alert!!!", message: "Do you want to send FIST AID KIT to your current location?", preferredStyle: UIAlertController.Style.alert);
        let yesButton = UIAlertAction(title: "Yes", style: UIAlertAction.Style.default) {
            action in
            self.getUserLocation()
            self.packageType = "firstAidPack"
            self.dataBase.document("location").setData([
                "situation": true,
                "packageType": self.packageType
            ]) { err in
                if let err = err {
                    print("Error writing document: \(err)")
                } else {
                    print("Document successfully written!")
                }
            }
        }
        
        let noButton = UIAlertAction(title: "No", style: UIAlertAction.Style.destructive) {
            action in
        }
        alert.addAction(noButton);
        alert.addAction(yesButton);
        self.present(alert, animated: true, completion: nil)
    }
}

extension ViewController: CLLocationManagerDelegate {
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        if let location = locations.last {
            self.location = ["latitude": location.coordinate.latitude,"longitude": location.coordinate.longitude]
            
            dataBase.document("location").updateData([
                "currentLocation": [self.location] //arrayUnion -> update data method
                //"packageType": self.packageType
            ]) { err in
                if let err = err {
                    print(err)
                }
            }
            
            let location = "Lat : \(location.coordinate.latitude) \nLng : \(location.coordinate.longitude)"
            
            print(location)
        }
    }
}


