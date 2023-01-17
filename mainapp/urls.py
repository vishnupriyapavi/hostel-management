from django.urls import path

from mainapp import views, admin_views, student_views, parent_views

urlpatterns=[
    path('',views.index,name='index'),
    path('Login', views.Login, name='Login'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('admin1',views.admin1,name='admin1'),
    path('student', views.student, name='student'),
    path('parents', views.parents, name='parents'),

    path('reg_stu',views.reg_stu,name='reg_stu'),
    path('par_reg',views.par_reg,name='par_reg'),

    path('student_view',admin_views.student_view,name='student_view'),
    path('approval_student/<int:id>/',admin_views.approve_student,name='approval_student'),
    path('reject_student/<int:id>/',admin_views.reject_student,name='reject_student'),

    path('parent_view',admin_views.parent_view,name='parent_view'),
    path('approve_parent/<int:id>',admin_views.approve_parent,name='approve_parent'),
    path('reject_parent/<int:id>',admin_views.reject_parent,name='reject_parent'),

    path('add_hostel',admin_views.add_hostel,name='add_hostel'),
    path('view_hostel',admin_views.view_hostel,name='view_hostel'),
    path('hostel_update/<int:id>', admin_views.hostel_update, name='hostel_update'),
    path('hostel_delete/<int:id>', admin_views.hostel_delete, name='hostel_delete'),

    path('admin_add_room', admin_views.admin_add_room, name='admin_add_room'),
    path('admin_view_room',admin_views.admin_view_room,name='admin_view_room'),
    path('approve_booking/<int:id>',admin_views.approve_booking,name='approve_booking'),
    path('reject_booking/<int:id>',admin_views.reject_booking,name='reject_booking'),


    path('add_food',admin_views.add_food,name='add_food'),
    path('view_food',admin_views.view_food,name='view_food'),
    path('food_update/<int:id>', admin_views.food_update, name='food_update'),
    path('food_delete/<int:id>', admin_views.food_delete, name='food_delete'),

    path('add_staff', admin_views.add_staff, name='add_staff'),
    path('view_staff', admin_views.view_staff, name='view_staff'),
    path('staff_update/<int:id>', admin_views.staff_update, name='staff_update'),
    path('staff_delete/<int:id>', admin_views.staff_delete, name='staff_delete'),

    path('add_notification', admin_views.add_notification, name='add_notification'),
    path('view_notification', admin_views.view_notification, name='view_notification'),
    path('notification_update/<int:id>', admin_views.notification_update, name='notification_update'),
    path('notification_delete/<int:id>', admin_views.notification_delete, name='notification_delete'),


    path('add_fee', admin_views.add_fee, name='add_fee'),
    path('view_fee', admin_views.view_fee, name='view_fee'),
    path('fee_update/<int:id>', admin_views.fee_update, name='fee_update'),
    path('fee_delete/<int:id>', admin_views.fee_delete, name='fee_delete'),

    path('view_complaint',admin_views.view_complaint,name='view_complaint'),
    path('reply_com/<int:id>',admin_views.reply_com,name='reply_com'),

    # path('comp_update/<int:id>',admin_views.comp_update,name='comp_update'),
    # path('comp_delete/<int:id>',admin_views.comp_delete,name='comp_delete'),

    path('view_review',admin_views.view_review,name='view_review'),
    path('review_delete/<int:id>', admin_views.review_delete, name='review_delete'),

    path('add_attendance',admin_views.add_attendance,name='add_attendance'),
    path('view_attendance',admin_views.view_attendance,name='view_attendance'),
    path('attendance_update/<int:id>', admin_views.attendance_update, name='attendance_update'),
    path('attendance_delete/<int:id>', admin_views.attendance_delete, name='attendance_delete'),

    path('add_admin_pay', admin_views.add_admin_pay, name='add_admin_pay'),
    path('view_pay', admin_views.view_pay, name='view_pay'),
    path('pay_delete/<int:id>', admin_views.pay_delete, name='pay_delete'),
    path('pay_update/<int:id>', admin_views.pay_update, name='pay_update'),

    path('student_view_hostel', student_views.student_view_hostel, name='student_view_hostel'),
    path('student_view_food', student_views.student_view_food, name='student_view_food'),
    path('student_view_fee', student_views.student_view_fee, name='student_view_fee'),

    path('student_add_complaint', student_views.student_add_complaint, name='student_add_complaint'),
    path('student_view_reply', student_views.student_view_reply, name='student_view_reply'),
    path('student_add_review', student_views.student_add_review, name='student_add_review'),

    path('view_studpay', student_views.view_studpay, name='view_studpay'),
    path('approve_payment/<int:id>', student_views.approve_payment, name='approve_payment'),
    path('reject_payment/<int:id>', student_views.reject_payment, name='reject_payment'),

    path('parent_view_hostel', parent_views.parent_view_hostel, name='parent_view_hostel'),
    path('parent_view_attendance', parent_views.parent_view_attendance, name='parent_view_attendance'),
    path('parent_view_staff', parent_views.parent_view_staff, name='parent_view_staff'),
    path('parent_view_fee', parent_views.parent_view_fee, name='parent_view_fee'),

    path('room_booking', student_views.room_booking, name='room_booking'),
    path('view_room', student_views.view_room, name='view_room'),
    # path('student_approve_room/<int:id>', student_views.student_approve_room, name='student_approve_room'),
    # path('student_reject_room/<int:id>', student_views.student_reject_room, name='student_reject_room'),
    path('student_update_room/<int:id>', student_views.student_update_room, name='student_update_room'),
    path('delete_room/<int:id>', student_views.delete_room, name='delete_room'),

    path('student_view_profile', student_views.student_view_profile, name='student_view_profile'),
    path('student_update_profile', student_views.student_update_profile, name='student_update_profile'),

    path('student_view_attendance', student_views.student_view_attendance, name='student_view_attendance'),

    path('parent_view_room', parent_views.parent_view_room, name='parent_view_room'),
    path('parent_view_pay', parent_views.parent_view_pay, name='parent_view_pay'),


    path('delete_profile_student', student_views.delete_profile_student, name='delete_profile_student'),
    path('delete_profile_parent', parent_views.delete_profile_parent, name='delete_profile_parent'),










]